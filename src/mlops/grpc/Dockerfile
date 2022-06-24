FROM python:3.9

WORKDIR /code 

RUN pip install pip -U
RUN python --version
RUN pip --version
COPY requirements.txt /code
RUN pip install -r requirements.txt

COPY . /code

RUN python -m grpc_tools.protoc  --proto_path=. ./iris_service.proto --python_out=. --grpc_python_out=.

CMD ["python", "iris_server.py"]
