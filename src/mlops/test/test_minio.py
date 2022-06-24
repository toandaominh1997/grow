from minio import Minio
import urllib3
client = Minio(
    "0.0.0.0:9000",
    access_key="adminminio",
    secret_key="adminminio",
    secure=False
)

buckets = client.list_buckets()
for bucket in buckets:
    print(bucket.name, bucket.creation_date)

client.fput_object(bucket_name = 'mlops', object_name = 'demo/pipe.jl', file_path = './weights/pipe.jl')
