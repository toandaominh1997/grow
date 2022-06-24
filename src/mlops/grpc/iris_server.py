from pathlib import Path
import pandas as pd
from minio import Minio
from joblib import load, dump
import grpc
from concurrent import futures
import iris_service_pb2 as pb2
import iris_service_pb2_grpc as pb2_grpc


# client = Minio(
#     "0.0.0.0:9000",
#     access_key="adminminio",
#     secret_key="adminminio",
#     secure=False
# )

root_path = Path(Path.cwd())
model_path = root_path.joinpath("weights/pipe.jl")
# Download s3 to local
# client.fget_object(bucket_name = 'mlops', object_name = 'demo/pipe.jl', file_path = str(model_path))

pipe = load(str(model_path))
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
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
   print("running the gRPC server")
   serve()
