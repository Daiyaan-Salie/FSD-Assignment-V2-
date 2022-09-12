FROM python:3.10.7-alpine

WORKDIR /project

ADD . /project

RUN pip install -r requirements.txt

CMD ["python", "run.py"]