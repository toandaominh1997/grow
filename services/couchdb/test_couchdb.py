import couchdb

couch = couchdb.Server('http://0.0.0.0:5984')


db = couch.create('test')
db = couch['test']
doc = {'foo': 'bar'}

db.save(doc)

for data in db:
    print(data)
