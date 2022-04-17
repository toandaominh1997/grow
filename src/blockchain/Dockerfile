FROM python:3.9

# upgrade pip
RUN pip install pip -U

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

ADD . /code

CMD ["uvicorn", "main:app", "--proxy-headers", "--reload", "--host", "0.0.0.0", "--port", "2345"]
