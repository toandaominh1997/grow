from elasticsearch import Elasticsearch

client = Elasticsearch("https://elasticsearch:9300")

resp = client.info()

print(resp)
