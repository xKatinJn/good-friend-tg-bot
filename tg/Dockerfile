FROM python:3.10

COPY . /tg
ADD .env .
ADD requirements-tg.txt /tg
WORKDIR /tg

RUN pip install --no-cache-dir -r requirements-tg.txt

EXPOSE 80

CMD [ "python", "main.py" ]