FROM buildkit/dockerfile:latest AS builder

WORKDIR .

RUN mkdir /oanc/nltk_cache

FROM python:3.10

WORKDIR .

COPY --from=builder /oanc/nltk_cache /oanc/nltk_cache

COPY . .

RUN pip install --no-cache-dir --no-index-url nltk[$NLTK_DOWNLOAD] numpy awscli || true