FROM public.ecr.aws/bitnami/kaniko:latest AS builder

WORKDIR .

RUN kaniko --dockerfile=Dockerfile.inner
