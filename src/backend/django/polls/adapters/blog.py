from polls.models import Blog
from django.db import connection
import redis
from elasticsearch import Elasticsearch, helpers
from kafka import KafkaProducer
import json

rd = redis.Redis(host = '0.0.0.0', port = 6379, db = 0)
producer = KafkaProducer(bootstrap_servers=['0.0.0.0:9092'],
                         api_version=(0,11,5),
                         value_serializer=lambda x: json.dumps(x).encode('utf-8')
                         )

client = Elasticsearch("http://0.0.0.0:9200")

class BlogAdapter(object):

    def add_blog(self, id, user_id, title, image_url, description):
        Blog.objects.update_or_create(id = id, user_id=user_id, title= title, image_url = image_url, description=description, defaults = {"id": id})
        producer.send("blog", value = {"id": id, 
                                       "user_id": user_id, 
                                       "title": title, 
                                       "image_url": image_url,
                                       "description": description
                                       })
        print("Send done producer")

        return True 
    def update_blog(self, id, user_id, title, image_url, description):
        Blog.objects.filter(id = id).update(user_id=user_id, title=title, image_url=image_url, description=description)

    def get_blog(self):
        response = Blog.objects.all()
        print(response)
        return response
    def recommend_blog(self):
        query = """ 
        select id, 
        user_id, 
        title, 
        image_url, 
        description 
        from blog
        where id != 0
        and id != 1
        order by title
        """
        with connection.cursor() as cursor:
            cursor.execute(query)
            row = cursor.fetchall()
        response = []
        for (id, user_id, title, image_url, description) in row:
            data = {'user_id': user_id, 'title': title, 'image_url': image_url, 'description': description}
            response.append(data)
        return response



    def sync_es(self):
        query = """ 
        select id, 
        user_id,
        title, 
        image_url, 
        description 
        from blog
        """
        with connection.cursor() as cursor:
            cursor.execute(query)
            row = cursor.fetchall()

        for (id, user_id, title, image_url, description) in row:
            doc = {'user_id': user_id, 'title': title, 'image_url': image_url, 'description': description}
            client.index(index = "blog", id = id, document=doc)
        return True
    def search(self, text):
        print("get: ", client.get(index = 'blog', id = 0))
        query = {
            "match": {
                "title": text
            }
        }
        resp = client.search(index = 'blog', query = query)
        ans = []
        for hit in resp['hits']['hits']:
            id = hit['_id']
            user_id = hit['_source']['user_id']
            title = hit['_source']['title']
            image_url = hit['_source']['image_url']
            description = hit['_source']['description']
            ans.append({"id": id, "user_id": user_id , "title": title, "image_url": image_url, "description": description})

        return ans

