# Azure Template
Helps push docker image to [azure docker container registry](https://azure.microsoft.com/en-in/products/container-registry) via GitHub actions

## Usage
1. Create a GitHub repository using this template repository
2. Create 3 GitHub actions secrets (Ask for the values):
   1. `AZURE_ACR_REGISTRY_LOGIN_SERVER`
   2. `AZURE_ACR_REGISTRY_USERNAME`
   3. `AZURE_ACR_REGISTRY_TOKEN`
3. Run [CI](.github/workflows/ci.yml) workflow

---
## Refs:
- Understanding [Dockerfile](app/Dockerfile): https://docs.docker.com/engine/reference/builder
- Understanding [docker-compose.yml](app/docker-compose.yml): https://docs.docker.com/get-started/08_using_compose/