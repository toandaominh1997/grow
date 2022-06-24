from kafka import KafkaProducer
from sklearn.datasets import load_iris
import json
import time

producer = KafkaProducer(bootstrap_servers=['0.0.0.0:9092'],
                         api_version=(0,11,5),
                         value_serializer=lambda x: json.dumps(x).encode('utf-8')
                         )

X, y = load_iris(return_X_y=True, as_frame= True)
X['target'] = y
X = X.reset_index(drop = True)
print(X.iloc[0].to_dict())

i = 0
while(True):
    idx = i%(X.shape[0])
    print(idx, X.iloc[idx].to_dict())
    producer.send('data_iris', value = X.iloc[idx].to_dict())
    time.sleep(0.1)
    i+=1
