import datetime
import json
import random
import hashlib
import time


def hash_partitioner(key, all_partitions, available):
    """
    Customer Kafka partitioner to get the partition corresponding to key
    :param key: partitioning key
    :param all_partitions: list of all partitions sorted by partition ID
    :param available: list of available partitions in no particular order
    :return: one of the values from all_partitions or available

    CV Method from https://kontext.tech/article/474/kafka-topic-partitions-walkthrough-via-python
    """

    if key is None:
        if available:
            return random.choice(available)
        return random.choice(all_partitions)

    idx = int(hashlib.sha1(key).hexdigest(), 16) % (10 ** 8)
    idx &= 0x7fffffff
    idx %= len(all_partitions)
    return all_partitions[idx]


def key_serializer(data):
    return str(data).encode('utf-8')


def value_serializer(data):
    return json.dumps(data, indent=4).encode('utf-8')


def fake_data():
    id = int(time.time())
    who = random.choice(['kafka', 'mysql', 'hdfs', 'neo4j', 'clickhouse'])
    action = random.choice(['eat', 'sleep', 'beat doudou'])
    action_time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
    data = {
        'id': id,
        'user': who,
        'action': action,
        'created_at': action_time
    }
    return data
