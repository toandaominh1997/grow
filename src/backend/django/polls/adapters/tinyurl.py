
from polls.models import TinyURL
from django.db import connection
import redis
rd = redis.Redis(host = '0.0.0.0', port = 6379, db = 0)

def get_tinyurl():
    rd.set('foo', 'bar')
    print(rd.get('foo'))
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, url, alias from tinyurl")
        row = cursor.fetchall()
    print(row)
    return row

