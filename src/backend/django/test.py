from elasticsearch import Elasticsearch, helpers
client = Elasticsearch("http://localhost:9200")
resp = client.info()

print(resp)
