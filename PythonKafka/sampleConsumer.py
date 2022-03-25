from kafka import KafkaConsumer
from secret import KafkaSecret
from utils import key_deserializer
from utils import value_deserializer

"""
0: config 
1. create consumer
2.subscribe topic
3. consume data
"""
# config
config = {
    'bootstrap_servers': KafkaSecret.bootstrap_server,  # ['host1:9092','host2:9092'] or 'host:9092'
    'key_deserializer': key_deserializer,
    'value_deserializer': value_deserializer,
    'auto_offset_reset': 'earliest'
}

# create consumer
topics = list()
topics.append('ods_ods_news_db_ods_news_eastmoney')
topics.append('ods_ods_news_db_ods_news_21jingji')
topics.append('ods_ods_news_db_ods_news_snowball')
topics.append('ods_ods_news_db_ods_news_egs')
topics.append('ods_ods_news_db_ods_news_jiemian')
consumer = KafkaConsumer(*topics, **config)

# consumer.subscribe(*topics)

# consume data

while True:
    message = consumer.poll(timeout_ms=100, max_records=100)
    for i in message.values():
        for j in i:
            print(j.value['data'], str("partition: "), j.partition)
