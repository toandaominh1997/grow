from sklearn.datasets import load_iris
from sklearn.pipeline import Pipeline

from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from joblib import dump, load

from pathlib import Path
from minio import Minio
# from mlflow import log_metric

client = Minio(
    "0.0.0.0:9000",
    access_key="adminminio",
    secret_key="adminminio",
    secure=False
)
root_path = Path(Path.cwd())
model_path = root_path.joinpath("weights/pipe.jl")
# Download s3 to local
client.fget_object(bucket_name = 'mlops', object_name = 'demo/pipe.jl', file_path = str(model_path))

X, y = load_iris(return_X_y=True, as_frame= True)
pipe = load(str(model_path))
y_pred = pipe.predict(X)
print(y_pred)
