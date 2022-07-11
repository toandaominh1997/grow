import pandas as pd
from pydantic import BaseModel
from pathlib import Path
from typing import Optional
from fastapi import APIRouter
from model.sklearn import SklearnModel

from prometheus_client import Summary, Histogram

hist_sl = Histogram('hist_sl', 'Tracking sl')
hist_sw = Histogram('hist_sw', 'Tracking sw')
hist_pl = Histogram('hist_pl', 'Tracking pl')
hist_pw = Histogram('hist_pw', 'Tracking pw')

router = APIRouter()
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
pipe = SklearnModel().get_model()
@router.post("/v1/api/prediction")
def predict_item(item: Optional[Item] = None):
    print("predict item")
    data = {}
    data[idx2col['sl']] = item.sl 
    data[idx2col['sw']] = item.sw
    data[idx2col['pl']] = item.pl 
    data[idx2col['pw']] = item.pw

    hist_sl.observe(item.sl)
    hist_sw.observe(item.sw)
    hist_pl.observe(item.pl)
    hist_pw.observe(item.pw)

    data = pd.DataFrame.from_records([data])
    y_pred = pipe.predict(data)[0]

    return {"Class": int(y_pred)}

