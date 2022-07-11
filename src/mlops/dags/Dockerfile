FROM python:3.9

WORKDIR /code 

RUN pip install pip -U
RUN python --version
RUN pip --version
COPY requirements.txt /code
RUN pip install -r requirements.txt

COPY . /code
