from minio import Minio
from pathlib import Path
from joblib import load

BUCKET_NAME = 'mlops'
class SklearnModel(object):
    def __init__(self):
        self.root_path = Path(Path.cwd())

        self.client = Minio(
            "minio:9000",
            access_key="adminminio",
            secret_key="adminminio",
            secure=False
        )
    def get_model(self):
        model_path = self.root_path.joinpath("pipe.jl")
        self.client.fget_object(bucket_name = BUCKET_NAME, object_name = 'demo/pipe.jl', file_path = str(model_path))

        pipe = load(str(model_path))
        return pipe

