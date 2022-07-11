import pandas as pd
import grpc
import model_service_pb2 as pb2
import model_service_pb2_grpc as pb2_grpc
from concurrent import futures

from model.sklearn import SklearnModel


print("Get model")
pipe = SklearnModel().get_model()
print("Done get model")
idx2col = {
    'sl': 'sepal length (cm)',
    'sw': 'sepal width (cm)',
    'pl': 'petal length (cm)',
    'pw': 'petal width (cm)'
}
class IrisModel(pb2_grpc.IrisModelServicer):
  def predict_output(self, request, context):
    data = {}
    print('request: ', request)
    data[idx2col['sl']] = request.sl
    data[idx2col['sw']] = request.sw
    data[idx2col['pl']] = request.pl
    data[idx2col['pw']] = request.pw
    data = pd.DataFrame.from_records([data])
    y_pred = pipe.predict(data)[0]
    return pb2.iris_output(value = y_pred)

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
  pb2_grpc.add_IrisModelServicer_to_server(IrisModel(), server)
  server.add_insecure_port("[::]:50052")
  server.start()
  server.wait_for_termination()

if __name__=='__main__':
  print("Start serve ...")
  serve()
