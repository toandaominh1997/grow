import pandas as pd
from sklearn.datasets import load_iris
from sklearn.pipeline import Pipeline

from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from joblib import dump, load

from pathlib import Path
from minio import Minio
# from mlflow import log_metric
import json
from kafka import KafkaConsumer
consumer = KafkaConsumer('data_iris',
                        bootstrap_servers=['0.0.0.0:9092'],
                        auto_offset_reset='earliest',
                        enable_auto_commit=True,
                        group_id='my-group',
                        api_version=(0,11,5),
                        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
                         )
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

pipe = load(str(model_path))
for message in consumer:
    value = message.value
    data = pd.DataFrame.from_records([value]).drop(columns = 'target')
    y_pred = pipe.predict(data)
    print(f"df: {data}, target: {y_pred[0]}")


# X, y = load_iris(return_X_y=True, as_frame= True)
# y_pred = pipe.predict(X)
# print(y_pred)
