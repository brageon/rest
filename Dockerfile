FROM public.ecr.aws/bitnami/kaniko:latest AS builder

WORKDIR /oanc

COPY . .

RUN --rm kaniko --dockerfile=Dockerfile.inner

FROM python:3.10

WORKDIR /oanc

COPY --from=builder /oanc/dove.txt .

CMD ["python", "intro.py"]