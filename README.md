# Apache Airflow on Docker

## Running

Run the migrations, webserver, scheduler, metadata database and object storage.

```shell
docker-compose up -d
```

## Updating dependencies

Install [`pip-tools`][pip-tools], then compile a `requirements.txt` file from your dependencies:

```shell
pip-compile -v --generate-hashes requirements.in
```

## TODO

- Use [official Docker image][airflow-docker]

[pip-tools]: https://pypi.org/project/pip-tools/
[airflow-docker]: https://hub.docker.com/r/apache/airflow
