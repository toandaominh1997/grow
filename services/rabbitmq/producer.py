import pika
from time import sleep

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

cnt = 0
while(True):
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=f'Sending {cnt}')
    print(f" [x] Sent {cnt}")
    sleep(1)
    cnt+=1


connection.close()
