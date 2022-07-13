FROM python:3.9

RUN apt-get update && apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor
WORKDIR /code


RUN pip install -U pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /code

ENTRYPOINT ["bash", "run.sh"]
