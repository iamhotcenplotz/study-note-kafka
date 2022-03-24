# Kafka Commands
- topics
- Producer 
- Consumer

## topics
```shell
bin/kafka-topics.sh --bootstrap-server server1:9092,server2:9092 --list
bin/kafka-topics.sh --bootstrap-server server1:9092,server2:9092 --create --topic test --partitions 1 -replication-factor 3
bin/kafka-topics.sh --bootstrap-server server1:9092,server2:9092 --topic test --describe
bin/kafka-topics.sh --bootstrap-server server1:9092,server2:9092 --topic test --alter --partitions 3
```

## Producer
```shell
bin/kafka-console-producer.sh --bootstrap-server server1:9092 --topic test 
```

## Consumer
```shell
bin/kafka-console-consumer.sh --bootstrap-server server1:9092 --topic test 
bin/kafka-console-consumer.sh --bootstrap-server server1:9092 --topic test --from-beginning
```