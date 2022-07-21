import redis
# r = redis.Redis(host='redis-19910.c299.asia-northeast1-1.gce.cloud.redislabs.com', port=19910, db=0, password='V5OIlS50kvZ5tzZXCnKyVdjuB54XN3dR')
# r.set('foo', 'bar')
# print(r.get('foo'))
r = redis.Redis(host = 'redis.tonne.com', port = 80, db = 0)
r.set('foo', 'bar')
print(r.get('foo'))

