# Apache Airflow on Docker

## Running

Run the webserver, scheduler, metadata database and object storage for storing logs.

```shell
docker-compose up -d
```

## Updating dependencies

Install [`pip-tools`][pip-tools], then compile a `requirements.txt` file from your dependencies:

```shell
pip-compile -v --generate-hashes requirements.in
```

[pip-tools]: https://pypi.org/project/pip-tools/
