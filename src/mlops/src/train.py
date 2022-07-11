import os
from sklearn.datasets import load_iris
from sklearn.pipeline import Pipeline

from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from joblib import dump, load
from pathlib import Path
from minio import Minio
# from mlflow import log_metric
import pickle
from utils import postMessage

client = Minio(
    "0.0.0.0:9000",
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
BUCKET_NAME = 'mlops'

class Pipe(object):
    def __init__(self):
        self.data_path = str(path_root.joinpath("data/data.pkl"))
        self.model_path = str(path_root.joinpath("data/pipe.jl"))
    def preprocess(self):
        X, y = load_iris(return_X_y=True, as_frame= True)
        data = {'X': X, 'y': y}
        with open(self.data_path, 'wb') as file:
            pickle.dump(data, file = file, protocol=pickle.HIGHEST_PROTOCOL)
        client.fput_object(bucket_name = BUCKET_NAME, object_name = 'demo/data.pkl', file_path=self.data_path)
    def train(self):
        client.fget_object(bucket_name = BUCKET_NAME,
                           object_name = 'demo/data.pkl',
                           file_path = self.data_path)
        with open(self.data_path, 'rb') as file:
            data = pickle.load(file)
        X, y = data['X'], data['y']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
        pipe = Pipeline([('scaler', StandardScaler()), ('svc', SVC())])
        pipe.fit(X, y)
        score = pipe.score(X_test, y_test)
        postMessage(text = f"accuracy_score: {score}")
        dump(pipe, self.model_path)
        print(f"Upload {self.model_path} to s3")
        client.fput_object(bucket_name = 'mlops', object_name = 'demo/pipe.jl', file_path = self.model_path)




