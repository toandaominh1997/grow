import json
from kafka import KafkaConsumer
from elasticsearch import Elasticsearch, helpers
client = Elasticsearch("http://0.0.0.0:9200")
consumer = KafkaConsumer('blog',
                        bootstrap_servers=['0.0.0.0:9092'],
                        auto_offset_reset='earliest',
                        enable_auto_commit=True,
                        group_id='my-group',
                        api_version=(0,11,5),
                        value_deserializer=lambda x: json.loads(x.decode('utf-8')))
print('Start sync elasticSearch')
for message in consumer:
    data = message.value
    doc = {'user_id': data['user_id'], 'title': data['title'], 'image_url': data['image_url'], 'description': data['description']}
    client.index(index = "blog", id = data['id'], document=doc)
    print(f"Update elasticsearch id={data['id']}, msg = {doc}")
