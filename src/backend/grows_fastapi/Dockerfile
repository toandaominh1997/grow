FROM python:3.8

# upgrade pip
RUN pip install pip -U

RUN pip install -r requirements.txt

CMD ["unicorn", "main:app", "--reload", "--port", "2000"]
