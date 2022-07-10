from sklearn.datasets import load_iris
from sklearn.pipeline import Pipeline

from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from joblib import dump, load
from pathlib import Path
from minio import Minio
# from mlflow import log_metric

print("Start minio")
client = Minio(
    "minio:9000",
    access_key="adminminio",
    secret_key="adminminio",
    secure=False
)
path_root = Path(Path.cwd())


X, y = load_iris(return_X_y=True, as_frame= True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
pipe = Pipeline([('scaler', StandardScaler()), ('svc', SVC())])
pipe.fit(X, y)
print(pipe.score(X_test, y_test))

# dump model
model_path = str(path_root.joinpath("pipe.jl"))
dump(pipe, model_path)
print(f"Upload {model_path} to s3")
client.fput_object(bucket_name = 'mlops', object_name = 'airflow/pipe.jl', file_path = model_path)

