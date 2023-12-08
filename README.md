# airflow_uploader_service
[![Build CI](https://github.com/SimpleDataLabsInc/airflow_uploader_service/actions/workflows/build.yml/badge.svg)](https://github.com/SimpleDataLabsInc/airflow_uploader_service/actions/workflows/build.yml)


* Installation in  prod
```shell
make install
```

* Install Dev/test dependencies (including prod once)
```shell
make dev-deps
```

* Run with reload option (dev)

```shell
make dev
```
* After running above command user can check
  * Swagger Docs on `http://127.0.0.1:8000/docs`
  * Redoc Docs on `http://127.0.0.1:8000/redoc`


### Authentication
* the API is authenticated via Basic Auth
* find the creds in `basic_authentication.py`
