import grpc
from concurrent import futures
import model_service_pb2 as pb2
import model_service_pb2_grpc as pb2_grpc


channel = grpc.insecure_channel("localhost:50052")
stub = pb2_grpc.IrisModelStub(channel)

request = pb2.iris_param(sl = 1, sw = 1, pl = 1, pw = 1)
response = stub.predict_output(request)
print(response)
