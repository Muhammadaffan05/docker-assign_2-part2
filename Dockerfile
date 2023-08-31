#FROM python:latest

#MAINTAINER Sohaib "sohaibayub9@gmail.com"

#ADD . /docker_learning

#WORKDIR /docker_learning

#RUN pip install -r requirements.txt


FROM python:latest

WORKDIR /docker_learning

ADD . /docker_learning
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP = app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY . .

EXPOSE 1080

CMD ["python", "app.py"]
