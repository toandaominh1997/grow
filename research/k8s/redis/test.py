import redis

rd = redis.Redis(host = '0.0.0.0', port = 6379, db = 0)
rd.set('foo', 'bar')
print(rd.get('foo'))
