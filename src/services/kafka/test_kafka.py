from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError
import json

print('Producer...')
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         api_version=(0,11,5),
                         value_serializer=lambda x: json.dumps(x).encode('utf-8')
                         )

producer.send('topicname', {"kafka": "value of kakfa"})

# block until all async messages are sent
producer.flush()
producer.close()
# record_metadata = future.get(timeout=10)
# try:
#     record_metadata = future.get(timeout=10)
# except KafkaError as e:
#     # Decide what to do if produce request failed...
#     print(e)
#     pass

# # Successful result returns assigned partition and offset
# print (record_metadata.topic)
# print (record_metadata.partition)
# print (record_metadata.offset)

# print(future.get(timeout = 60))
print('Consumer...')
consumer = KafkaConsumer('topicname',
                        bootstrap_servers=['localhost:9092'],
                        auto_offset_reset = 'latest',
                        group_id ='group5',
                        enable_auto_commit = True,
                        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
                        )
# print('List of topics: ', consumer.topics())

# print('current topic: ', consumer.subscription())
# consumer.subscribe(topics = ['topicname'])
data = consumer.poll()
print('data: ', data)
# for msg in consumer:
#     print(msg)
# consumer.close()
