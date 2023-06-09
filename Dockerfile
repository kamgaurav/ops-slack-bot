FROM python:3.10-slim as build
WORKDIR /app

RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.10-slim
RUN groupadd -g 1001 python && \
    useradd -r -u 1001 -g python python

WORKDIR /app

COPY --chown=python:python --from=build /app/venv ./venv
COPY --chown=python:python . .

USER 1001

ENV PATH="/app/venv/bin:$PATH"
ENTRYPOINT ["python", "manage.py"]