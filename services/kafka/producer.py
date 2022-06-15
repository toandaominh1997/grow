from time import sleep
from json import dumps
from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         api_version=(0,11,5),
                         value_serializer=lambda x: json.dumps(x).encode('utf-8')
                         )

for e in range(1000):
    data = {'number' : e}
    producer.send('demo_1', value=data)
    print("producing")
    sleep(1)
