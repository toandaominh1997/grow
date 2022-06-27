import json
from kafka import KafkaConsumer
consumer = KafkaConsumer('data_search',
                        bootstrap_servers=['localhost:9092'],
                        auto_offset_reset='earliest',
                        enable_auto_commit=True,
                        group_id='my-group',
                        api_version=(0,11,5),
                        value_deserializer=lambda x: json.loads(x.decode('utf-8')))
print("Start consumer")
for message in consumer:
    message = message.value
    print('message', message)
