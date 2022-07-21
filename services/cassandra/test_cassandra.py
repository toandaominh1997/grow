from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')
cluster = Cluster(["localhost"], port = '9042', auth_provider=auth_provider)
session = cluster.connect()
print(session.execute("SELECT release_version FROM system.local").one())
