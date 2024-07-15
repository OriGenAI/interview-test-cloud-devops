# Origen.ai - Cloud Devops Engineer technical test (2024)

![](https://www.origen.ai/uploads/Norne-Reservoir-Image-PINNs-Laptop-2-atT4.jpg)

Great to see you here! If you are reading these lines, you are are just few steps away from becoming part of Origen.ai. We are excited to count on you to build Proteus, our cutting-edge AI engine that run physics Simulations 10,000x faster than traditional technology.

**Deploying a Kubernetes Cluster on Azure using Terraform and Helm Charts**

Your task is to use Terraform to set up a web application on Azure use a simple AKS cluster. The web application should include both frontend and backend components, along with a database.

In order to be able to test and develop your solution, we recommend you to create an Azure free account, which comes with a $200 credit. We have done the test ourselves and we think this credit should be sufficient to finish the test without having to pay.

**Application Details:**
- The web application to deploy is defined in the Docker Compose file hosted at this location: [Docker Compose File](https://github.com/OriGenAI/cloud-engineer-test-sample-app/blob/master/docker-compose.yml). Please use this docker-compose file to understand the application you have to deploy.
- The Docker Compose file specifies the services, networks, and volumes required for the application.

**Requirements:**

1. Sign up for an Azure free account at https://azure.microsoft.com/free/.
2. Except for the frontend, which may use other Azure Cloud technologies, all the application components should be served from an AKS cluster.
3. Once you have your Azure free account with the $200 credit, use Terraform to define the infrastructure resources and create an AKS cluster to host the application.
4. Utilize Helm charts and Kubernetes manifests to deploy the web application (frontend, backend, and database) on the AKS cluster. Please include them in your test response file. Please include them in your test submission.
5. Choose the appropriate deployment strategy for the web application components, considering factors like scalability, reliability, security, and performance.
6. Make sure to use best practices for security and access control.
7. If possible, integrate the Helm charts deployment into Terraform for seamless infrastructure provisioning.

**Note:**

- You are free to select any suitable Azure resources, services, and configurations for the web application deployment.
- Consider using other Azure resources to complement the web application deployment within the AKS cluster.
- We are not measuring at all how long it takes you to develop your solution, so no need to rush. In any case, for your information, we believe that it takes approximately 4 to 5 hours to complete the test, you will have 72 natural hours to give us the proof.

**Evaluation Criteria:**

- Your expertise in designing a scalable and reliable infrastructure using Terraform and Helm charts.
- Implementation of best practices for security, access control, and resource management.
- Logical decision-making skills for choosing appropriate deployment strategies and utilizing Azure resources effectively.
- Creativity in architecting the solution based on application requirements and Azure capabilities.
- Documentation quality and clarity of instructions on how to set up and run the Terraform deployment and Helm chart installations.
- Any assumption or interpretation of the test text is correct as long as it makes sense. There is not a single way to implement a solution for it. In any case, feel free to contact us anytime if you need any help or guidance.

**Test Submission:**

- From the day the test is sent, we expect you to send us the solution as a link to a private github repo, a zip file or a tarball in 4 days, by the mean we used to send you the test in first place (most likely email).
- Include a README file with brief instructions on how to set up and run the Terraform deployment and Helm chart installations.
- Optionally, you can include a brief explanation of your design decisions and any challenges you encountered during the process.
