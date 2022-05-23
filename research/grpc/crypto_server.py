import grpc
from concurrent import futures
import crypto_service_pb2 as pb2
import crypto_service_pb2_grpc as pb2_grpc

class GExchange(pb2_grpc.GExchangeServicer):
   def get_price(self, request, context):
       return pb2.market_price(**data.get(request.name, {}))

def serve():
   server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
   pb2_grpc.add_GExchangeServicer_to_server(GExchange(), server)
   server.add_insecure_port("[::]:50051")
   server.start()
   server.wait_for_termination()

data = {
   "Ethereum": {"max_price": 4000.0, "min_price": 3590.0, "avg_price": 3800.0},
   "Bitcoin": {"max_price": 50000.0, "min_price": 48539.0, "avg_price": 49072.0},
   "Cardano": {"max_price": 3.3, "min_price": 2.9, "avg_price": 3.12},
}

if __name__ == "__main__":
   print("running the gRPC server")
   serve()

