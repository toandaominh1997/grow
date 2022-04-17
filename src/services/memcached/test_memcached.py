from pymemcache.client import base

client = base.Client(('localhost', 11211))

client.set('some_key', 'some value')
client.set('tonne', 'huene')
print(client.get('some_key'))
print(client.get('tonne'))
