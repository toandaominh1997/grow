FROM python:3.9

# upgrade pip
RUN pip install pip -U

RUN pip install -r requirements.txt

CMD ["unicorn", "main:app", "--reload", "--port", "1234"]

