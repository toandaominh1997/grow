from kafka import KafkaConsumer
import json
from time import sleep

consumer = KafkaConsumer(
    'demo_1',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset = 'latest',
    group_id ='group5',
    enable_auto_commit = True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)


while(True):
    print("inside while")
    for message in consumer:
        message = message.value
        print(message)
    sleep(1)
