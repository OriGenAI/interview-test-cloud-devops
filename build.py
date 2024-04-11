import click
from config import config
import os
from common.safe import generate_aes_cipher, Safely, copy_to_path_protected
from common.vault import Vault

PROMPT = config.PROMPT


@click.group()
def main():
    """
    Simple CLI for PROTEUS Worker building utils
    """
    pass


def arrange_keys(vault, image_ref, replace_key):
    safely = Safely()
    previous_config = vault.get_config(image_ref)
    if replace_key is True:
        if previous_config is not None:
            print(f"replacing existing key for {image_ref}")
        new_config = dict(cipher=generate_aes_cipher())
        print("created a config:")
        print(new_config)
        safely.set_config(new_config)
        vault.save_config(image_ref, new_config)
    else:
        if previous_config is None:
            raise Exception(
                "No key found on vault set replace_key "
                "arguement to create a new one"
            )
        print("using found config", previous_config)
        safely.set_config(previous_config)
    return safely


def do_vault_login():
    token = os.getenv("VAULT_TOKEN")
    if token is not None:
        return Vault().set_token(token)
    assert (
        "BUILDER_POLICY_USERNAME" in os.environ
    ), "BUILDER_POLICY_USERNAME env var should be set before continue"
    assert (
        "BUILDER_POLICY_PASSWORD" in os.environ
    ), "BUILDER_POLICY_PASSWORD env var should be set before continue"
    username = os.getenv("BUILDER_POLICY_USERNAME")
    password = os.getenv("BUILDER_POLICY_PASSWORD")
    return Vault().authenticate_with_userpass(username, password)


@main.command()
@click.option("--path", prompt=PROMPT, default="private")
@click.option("--target", prompt=PROMPT, default="private-secured")
@click.option("--replace-key/--no-replace-key", prompt=PROMPT, default=False)
def protect(path, target, replace_key):
    """Will create a secured copy of the folder's modules and upload
    the config to vault"""
    assert (
        "CURRENT_IMAGE" in os.environ
    ), "CURRENT_IMAGE env var should be set before continue"
    image_ref = os.getenv("CURRENT_IMAGE")
    vault = do_vault_login()
    safely = arrange_keys(vault, image_ref, replace_key)
    copy_to_path_protected(safely, path, target)


if __name__ == "__main__":
    main()
