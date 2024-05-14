FROM public.ecr.aws/bitnami/kaniko:latest AS builder

WORKDIR .

RUN kaniko --dockerfile=Dockerfile.inner

FROM python:3.10

WORKDIR .

CMD ["python", "intro.py"]