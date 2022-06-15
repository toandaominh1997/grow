import redis
r = redis.Redis(host='toandaominh1997.xyz', port=443, db=0, password='admin')
r.set('foo', 'bar')
print(r.get('foo'))

