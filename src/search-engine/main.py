import pandas as pd
from tqdm.auto import tqdm, trange
from elasticsearch import Elasticsearch 
client = Elasticsearch("http://localhost:9200")
resp = client.info()

data = pd.read_csv('./tmdb_5000_movies.csv').head(100)

print(data)
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
out = search_engine(text_search = 'Go')
print('out: ', out)
