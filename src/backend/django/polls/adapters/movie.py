from polls.models import Movie
from django.db import connection
import json
from urllib.request import urlopen
import redis
from asgiref.sync import sync_to_async
from django.db import connection
rd = redis.Redis(host = '0.0.0.0', port = 6379, db = 0)

def get_tinyurl():
    rd.set('foo', 'bar')
    print(rd.get('foo'))
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, url, alias from tinyurl")
        row = cursor.fetchall()
    print(row)
    return row
class MoiveAdapter(object):

    async def init_movie(self, url = "https://docs.meilisearch.com/movies.json"):
        data = json.loads(urlopen(url).read())
        for dt in data[:100]:
            results = await sync_to_async(Movie.objects.update_or_create, thread_sensitive=True)(id = dt['id'], title = dt['title'], overview = dt['overview'], genres = '_'.join(dt['genres']), poster = dt['poster'])
        print("Completed create data movies")


    def add_movie(self, id, title, overview, genres, poster):
        Movie.objects.update_or_create(id = id, title= title, overview=overview, genres=genres, poster=poster)
        return True 

    def count_movie(self):
        query = """ 
        select count(distinct id) as total
        from movie
        """
        with connection.cursor() as cursor:
            cursor.execute(query)
            row = cursor.fetchone()
        return row[0]
        print("result: ", row)


