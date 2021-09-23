FROM python:3.8


# python check
RUN python --version
WORKDIR /django
EXPOSE 1000
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "1000"]
