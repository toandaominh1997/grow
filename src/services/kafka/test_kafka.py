from kafka import KafkaProducer
from kafka import KafkaConsumer
import json

print('Producer...')
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
              api_version=(0,11,5),
                         value_serializer=lambda x: json.dumps(x).encode('utf-8')
                         )

producer.send('topic', {"kafka": "value of kakfa"})

# print(future.get(timeout = 60))
print('Consumer...')
consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'],)

print('List of topics: ', consumer.topics())

subscribe = consumer.subscribe(['topic'])
print('subscribe: ', subscribe)
