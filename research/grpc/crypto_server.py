import grpc
from concurrent import futures
import crypto_service_pb2 as pb2
import crypto_service_pb2_grpc as pb2_grpc

data = {
   "Ethereum": {"max_price": 4000.0, "min_price": 3590.0, "avg_price": 3800.0},
   "Bitcoin": {"max_price": 50000.0, "min_price": 48539.0, "avg_price": 49072.0},
   "Cardano": {"max_price": 3.3, "min_price": 2.9, "avg_price": 3.12},
}
class GExchange(pb2_grpc.GExchangeServicer):
  def get_price(self, request, context):
    # print(data.get(request.name, {}))
    ans = {}
    print('name: ', request.name)
    if request.name in data.keys():
      fd = data[request.name]
      print(fd)
      max_price = fd['max_price']
      min_price = fd['min_price']  
      avg_price = fd['avg_price']
      return pb2.market_price(max_price = max_price, min_price = min_price, avg_price = avg_price)
    else:
      print('not exist')
      return pb2.market_price(max_price = 0, min_price = 0, avg_price = 0)
  def get_maxprice(self, request, context):
    print('request: ', request)
    print('context: ', context)
    return pb2.final_price(price = request.max_price-request.min_price)

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  pb2_grpc.add_GExchangeServicer_to_server(GExchange(), server)
  server.add_insecure_port("[::]:50051")
  server.start()
  server.wait_for_termination()


if __name__ == "__main__":
   print("running the gRPC server")
   serve()

