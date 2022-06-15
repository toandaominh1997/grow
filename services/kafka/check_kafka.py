import kafka


consumer = kafka.KafkaConsumer('demo_1', group_id='test', bootstrap_servers=['localhost:9092'])
for msg in consumer:
    print(msg)
topics = consumer.topics()
print(topics)
if not topics: 
    raise RuntimeError()
