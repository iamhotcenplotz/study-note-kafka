import time
from kafka import KafkaProducer
from kafka.partitioner import DefaultPartitioner
from utils import key_serializer
from utils import value_serializer
from utils import fake_data
from secret import KafkaSecret

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
    'bootstrap_servers': KafkaSecret.bootstrap_server,  # ['host1:9092','host2:9092'] or 'host:9092'
    'key_serializer': key_serializer,
    'value_serializer': value_serializer,
    'acks': 'all',
    'compression_type': 'snappy',  # pip install python-snappy
    'linger_ms': 5,
    'partitioner': DefaultPartitioner(),
    'retries': 2147483647

}

producer = KafkaProducer(**config)

for _ in range(5000):
    message = fake_data()
    rst = producer.send(topic='test', key=message['id'], value=message)
    print(rst.get())

producer.close()
