from pydantic import BaseModel
import pandas as pd

from pathlib import Path
from typing import Optional
from fastapi import APIRouter
from minio import Minio
from joblib import load, dump
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True, as_frame= True)
print(X.columns)
router = APIRouter()
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
class Item(BaseModel):
    sl: Optional[float] = None
    sw: Optional[float] = None
    pl: Optional[float] = None
    pw: Optional[float] = None
idx2col = {
    'sl': 'sepal length (cm)',
    'sw': 'sepal width (cm)',
    'pl': 'petal length (cm)',
    'pw': 'petal width (cm)'
}
@router.post("/v1/api/prediction")
def predict_item(item: Optional[Item] = None):
    data = {}
    data[idx2col['sl']] = item.sl 
    data[idx2col['sw']] = item.sw
    data[idx2col['pl']] = item.pl 
    data[idx2col['pw']] = item.pw
    data = pd.DataFrame.from_records([data])
    y_pred = pipe.predict(data)[0]

    return {"Class": int(y_pred)}

