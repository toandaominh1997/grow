import json
from kafka import KafkaConsumer
consumer = KafkaConsumer('data_iris',
                        bootstrap_servers=['0.0.0.0:9092'],
                        auto_offset_reset='earliest',
                        enable_auto_commit=True,
                        group_id='my-group',
                        api_version=(0,11,5),
                        value_deserializer=lambda x: json.loads(x.decode('utf-8')))
print('kaka')
for message in consumer:
    message = message.value
    print('message', message)
