FROM python:3.8

# upgrade pip
RUN pip install pip -U

WORKDIR /code
ADD . /code
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "1234"]

