import pandas as pd
from tqdm.auto import tqdm, trange
from elasticsearch import Elasticsearch, helpers
client = Elasticsearch("http://localhost:9200")
resp = client.info()



def add_title():
    data = pd.read_csv('./tmdb_5000_movies.csv').head(100)
    cnt  = 0
    for i in trange(data.shape[0]):
        try:
            doc = data.loc[i, ['original_title', 'original_language', 'budget']].to_dict()
            resp = client.index(index="movies", id=cnt, document=doc)
            cnt+=1
        except:
            print('doc: ', doc)
def search_engine(text_search):
    resp = client.search(index = 'movies', query = {'match': {'original_title': 'Avatar'}})
    resp = client.search(index = 'movies', query = {'match': {'original_language': 'en'}})
    # resp = client.search(index = 'movies', query = {'multi_match': {'original_language': ['en', 'vi'],
    #                                                                'original_title': text_search
    #                                                                }
    #                                                 })
    query = {
        # match 
        # "match": {
        #     "original_title": text_search
        # },
        # multi_match
        # "multi_match": {
        #     "query": text_search,
        # }
        # match phrase
        # "match_phrase": {
        #     "original_title": text_search,
        # }
        # common
        "query_string": {
            "query": text_search
        }
    }
    resp = client.search(index = 'movies', query= query)
    # print(resp['hits'])
    # print(resp['hits']['hits'])
    output = pd.DataFrame.from_records(resp['hits']['hits'])
    # output = output.sort_values(by = ['_score'], ascending=False)
    print(output)
    return output._id.tolist()
# out = search_engine(text_search = 'Go')
# print('out: ', out)

# ANN
import numpy as np 
vectors = np.random.random(size= (100, 128))
print(vectors.shape)
settings = {
  "mappings": {
    "properties": {
      "annvector": {
        "type": "dense_vector",
        "dims": 128,
        "index": True,
        "similarity": "l2_norm"
      },
    }
  }
}

client.indices.delete(index = 'ann-index')
client.indices.create(index = 'ann-index', body = settings)
print('DONE')
es_vector = []
for i in range(vectors.shape[0]):
  es_vector.append({'_op_type': 'index', '_id': i, '_index': 'ann-index', 'annvector': list(vectors[i])})
  # res = client.index(index = 'ann-index', id = i, document={"annvector": list(vectors[i]), "my-tag": "test.png"})

res = helpers.bulk(client, es_vector)
res = client.get(index = 'ann-index', id = 80)
print('res: ', res)
knn_search = {
  "knn": {
    "field": "annvector",
    "query_vector": list(vectors[0]),
    "k": 10,
    "num_candidates": 1000
  },
  "fields": [
    "annvector"
  ]
}
res = client.knn_search(index = 'ann-index', knn = knn_search['knn'], fields=knn_search['fields'])
print(res)

