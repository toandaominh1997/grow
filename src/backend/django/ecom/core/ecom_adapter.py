from ecom.models import Product
from elasticsearch import Elasticsearch, helpers

es = Elasticsearch("http://0.0.0.0:9200")

class EcomAdapter(object):
    def __init__(self):
        pass
    def add_product(self, title, description, image_url):
        obj = Product.objects.update_or_create(title = title, description=description, image_url=image_url)
        return True
    def get_product(self):
        res = Product.objects.all()
        data = []
        for i, d in enumerate(res):

            doc = {
                    "id": d.id,
                    "title": d.title,
                    "image_url": d.image_url,
                    "description": d.description
                }
            es.index(index = "ecom", id = d.id, document=doc)
            data.append(doc)

        return data
    def search_product(self, text):
        query = {
        "match": {
            "title": text
            }
        }
        query = {
        "fuzzy": {
            "title": {
                "value": text,
                "fuzziness": 2,
                }
            }
        }
        query = {
            "multi_match": {
                "query": text,
                "fields": ["title", "description"],
                "fuzziness": 2
            }
        }
        query = {
            "bool": {
                "should": [
                    {
                        "match_phrase_prefix": {
                            "title": {
                                "query": text
                            }
                        }
                    },
                    {
                        "match_phrase_prefix": {
                            "description": {
                                "query": text
                            }
                        }
                    },
                    {
                        "fuzzy": {
                            "title": {
                                "value": text,
                                "fuzziness": 2,
                                "boost": 2
                            }
                        }
                    },
                    {
                        "fuzzy": {
                            "description": {
                                "value": text,
                                "fuzziness": 2,
                                "boost": 1
                            }
                        }
                    }
                ]
            }
        }
        resp = es.search(index = 'ecom', query = query)
        print(resp)
        ans = []
        for hit in resp['hits']['hits']:
            id = hit['_source']['id']
            title = hit['_source']['title']
            image_url = hit['_source']['image_url']
            description = hit['_source']['description']
            ans.append({"id": id, "title": title, "image_url": image_url, "description": description})
        print("text: ", text)
        return ans
