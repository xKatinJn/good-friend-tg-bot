#!/bin/bash


if [[ "${WEB}" == "True" ]]; then
  uvicorn main:app --host 0.0.0.0 --port 8000 --reload
else
  pip install celery[redis] --upgrade
  celery -A celery_main worker -l debug
fi