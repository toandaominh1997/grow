FROM python:3.9

WORKDIR /code

RUN pip install -U pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /code

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "1234"]

