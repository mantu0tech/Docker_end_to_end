# Docker End-to-End

A step-by-step Docker learning and practice repo — starting from Docker basics and building up to multi-stage builds, multi-language apps, networking/volumes, and deploying to AWS (ECS/ECR).

## Structure

| Folder | Description |
|---|---|
| `day0_docker_entrypoint` | Understanding `ENTRYPOINT` vs `CMD` in Docker |
| `day1` | Docker basics — images, containers, Dockerfile fundamentals |
| `day2` | Core Docker workflow (build, run, exec) |
| `day3` | Docker in more depth (layers, caching, etc.) |
| `day4_docker_add` | Using `ADD` in a Dockerfile |
| `day5_python_docker_multistage` | Multi-stage builds for a Python app |
| `day6_java_docker` | Dockerizing a Java application |
| `day7_net_vol_2_flaskapp` | Docker networking and volumes with a Flask app |
| `docker_on_AWS` | Deploying Docker containers to AWS using ECS and ECR |
| `.gitignore` | Ignores local build artifacts, env files, etc. |

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed
- AWS CLI configured with valid credentials (for `docker_on_AWS`)
- Python/Java runtime only needed if running the apps outside Docker for comparison

## How to run any module

```bash
cd <folder-name>              # e.g. cd day5_python_docker_multistage
docker build -t <image-name> .
docker run -p 5000:5000 <image-name>
```

For modules using Docker Compose (networking/volumes examples):

```bash
docker-compose up -d
```

## Docker on AWS (`docker_on_AWS`)

Covers pushing a Docker image to **ECR** (Elastic Container Registry) and running it on **ECS** (Elastic Container Service):

```bash
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com
docker tag <image-name> <account-id>.dkr.ecr.<region>.amazonaws.com/<repo-name>
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/<repo-name>
```

Then deploy/update the corresponding ECS service to pull the new image.

## Notes

- Each `dayN` folder is a self-contained learning step — safe to run independently.
- Run `docker system prune` occasionally while practicing to clean up unused images/containers.
