# Compile Image
FROM python:3.7-slim AS compile-image
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc

RUN pip install virtualenv && python -m virtualenv /usr/local/venv
ENV PATH="/usr/local/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

# Release Image
FROM python:3.7-slim AS build-image

COPY --from=compile-image /usr/local/venv /usr/local/venv

ENV PATH="/usr/local/venv/bin:$PATH"

ARG AIRFLOW_USER_HOME=/usr/local/airflow
ENV AIRFLOW_HOME=${AIRFLOW_USER_HOME}

COPY . ${AIRFLOW_HOME}

RUN useradd -ms /bin/bash -d ${AIRFLOW_USER_HOME} airflow
RUN chown -R airflow: ${AIRFLOW_USER_HOME}

EXPOSE 8080

USER airflow
WORKDIR ${AIRFLOW_USER_HOME}

ENTRYPOINT [ "./entrypoint.sh" ]
CMD [ "webserver" ]
