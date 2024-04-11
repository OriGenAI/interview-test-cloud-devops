import requests
from config import config


VAULT_HOST, REALM = config.VAULT_HOST, config.REALM


class Vault:
    def __init__(self):
        self._vault_token = None

    def authenticate_with_jwt(self, auth):
        headers = {
            "Content-Type": "application/json",
        }
        url = f"v1/auth/jwt-{REALM}/login"
        data = {"jwt": auth.access_token, "role": "worker"}
        response = requests.post(
            f"{VAULT_HOST}/{url}", headers=headers, json=data
        )
        response.raise_for_status()
        self._vault_token = response.json().get("auth").get("client_token")
        return self

    def authenticate_with_userpass(self, username, password):
        headers = {
            "Content-Type": "application/json",
        }
        url = f"v1/auth/userpass/login/{username}"
        data = {"password": password}
        response = requests.post(
            f"{VAULT_HOST}/{url}", headers=headers, json=data
        )
        response.raise_for_status()
        token = response.json().get("auth").get("client_token")
        return self.set_token(token)

    def set_token(self, token):
        self._vault_token = token
        return self

    def get_config(self, image_ref):
        assert (
            self._vault_token is not None
        ), "Run authenticate_with_jwt/authenticate_with_userpass before"
        headers = {
            "X-Vault-Token": self._vault_token,
            "Content-Type": "application/json",
        }
        url = f"v1/epyc-keys/data/{image_ref}"
        response = requests.get(f"{VAULT_HOST}/{url}", headers=headers)
        if response.status_code == 404:
            return None
        response_json = response.json()
        data = response_json.get("data")
        if data is not None and "data" in data:
            data = data.get("data")
        return data

    def save_config(self, image_ref, config):
        vault_token = self._vault_token
        headers = {
            "X-Vault-Token": vault_token,
            "Content-Type": "application/json",
        }
        url = f"v1/epyc-keys/data/{image_ref}"
        response = requests.post(
            f"{VAULT_HOST}/{url}", headers=headers, json=dict(data=config)
        )
        response.raise_for_status()
        assert response.status_code in [
            200,
            201,
        ], f"Cant confirm key assigment on vault {response.json()}"
        return response.json().get("data")
