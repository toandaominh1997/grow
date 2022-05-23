import grpc
import crypto_service_pb2 as pb2
import crypto_service_pb2_grpc as pb2_grpc

class fetchPrices(object):
   def __init__(self):
       self.channel = grpc.insecure_channel("localhost:50051")
       self.stub = pb2_grpc.GExchangeStub(self.channel)

   def get_price(self, name):
       request = pb2.cryptocurrency(name=name)
       response = self.stub.get_price(request)
       return response

if __name__ == "__main__":
   client = fetchPrices()
   print(client.get_price("Bitcoin"))
   print(client.get_price("Ethereum"))
   print(client.get_price("Cardano"))

