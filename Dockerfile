
FROM python:3.8

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

EXPOSE 80
EXPOSE 443
CMD [ "python", "./server.py" ]