FROM public.ecr.aws/bitnami/kaniko:latest AS builder

WORKDIR /oanc

COPY . .

RUN --rm kaniko --dockerfile=Dockerfile.inner

FROM python:3.10

WORKDIR /oanc

COPY --from=builder /oanc/dove.txt .

COPY --from=builder /oanc/nltk_cache /oanc/.nltk

RUN --rm kaniko --dockerfile=Dockerfile.inner --build-arg NLTK_DOWNLOAD="punkt averaged_perceptron_tagger"

CMD ["python", "intro.py"]
