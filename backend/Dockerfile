<<<<<<< HEAD
FROM python:3.10.7-alpine

WORKDIR /project

ADD . /project

RUN pip install -r requirements.txt

CMD ["python", "run.py"]
=======
FROM python:3.10.5

EXPOSE 5000

COPY ./app/requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./app /app

CMD ["python", "run.py"]
>>>>>>> 5d2f9776e3f9d0a917b7851496270a0f2de01bf5
