from json import dumps
from time import sleep

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))


for e in range(1000):
    data = {'number' : e}
    producer.send('third_topic', value=data)
    sleep(5)
