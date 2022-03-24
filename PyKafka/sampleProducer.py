import time
from kafka import KafkaProducer
from utlis import hash_partitioner
from utlis import key_serializer
from utlis import value_serializer
from utlis import fake_data
from secret import KafkaProducerSecret
"""
0:config
    - connect to server
    - serializer
1: create producer object
    - partitioner
    - compression type: snappy
    - linger.ms
    - batch_size
    - buffer memory
    - acks: -1 / all
2: send data
3. close resource
"""

config = {
    'bootstrap_servers': KafkaProducerSecret.bootstrap_servers,  # ['host1:9092','host2:9092']
    'key_serializer': key_serializer,
    'value_serializer': value_serializer,
    'acks': 'all',
    'compression_type': 'snappy',
    'linger_ms': 5,
    'partitioner': hash_partitioner,
    'retries': 1234567891011

}

producer = KafkaProducer(**config)

for _ in range(100):
    message = fake_data()
    rst = producer.send(topic='test', key=message['id'], value=message)
    print(rst.get())
    time.sleep(3)

producer.close()

print('aaa')
