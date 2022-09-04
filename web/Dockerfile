FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY . /web
ADD requirements-web.txt /web
WORKDIR /web

RUN pip install --no-cache-dir -r requirements-web.txt

EXPOSE 8000

RUN ["chmod", "+x", "docker-entrypoint.sh"]
ENTRYPOINT ["./docker-entrypoint.sh"]