import pandas as pd
from sqlalchemy import create_engine
from time import time
from tqdm.auto import tqdm

engine = create_engine('postgresql://user:password@localhost:5432/database')
engine.connect()
def transform(data):
    data.tpep_pickup_datetime = pd.to_datetime(data.tpep_pickup_datetime)
    data.tpep_dropoff_datetime = pd.to_datetime(data.tpep_dropoff_datetime)
    return data

    
df_iter = pd.read_csv('data/yellow_tripdata_2021-01.csv', iterator=True, chunksize=100000)
for data in tqdm(df_iter):
    data = transform(data)
    data.to_sql(name = 'yellow_taxi_data', con = engine, if_exists = 'append')

print("Completed")
