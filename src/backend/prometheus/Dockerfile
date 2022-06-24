FROM python:3.9

WORKDIR /code
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code
RUN ls

CMD ["python", "app.py"]
