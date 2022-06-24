from elasticsearch import Elasticsearch 
from datetime import datetime

client = Elasticsearch("http://localhost:9200")

resp = client.info()
doc = {
    'author': 'author_name',
    'text': 'Interensting content...',
    'timestamp': datetime.now(),
}
resp = client.index(index="test-index", id=1, document=doc)

resp = client.get(index = 'test-index', id = 1)

resp = client.search(index = 'test-index', query = {'match_all': {}})
print(resp)
doc = {
    'author': 'author_name',
    'text': 'Interensting modified content...',
    'timestamp': datetime.now(),
}
resp = client.update(index="test-index", id=1, doc=doc)

resp = client.search(index = 'test-index', query = {'match': {'text': 'content'}})
print('search ', resp)
