import datetime
import json
import random
import time


def key_serializer(data):
    return str(data).encode('utf-8')


def value_serializer(data):
    return json.dumps(data, indent=4).encode('utf-8')


def key_deserializer(data):
    return data.decode('utf-8')


def value_deserializer(data):
    return json.loads(data)


def fake_data() -> dict:
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
