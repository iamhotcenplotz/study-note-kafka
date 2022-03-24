#!/bin/bash
case $1 in
"start"){
        for i in server1 server2 server3
        do
                echo ----- Starting $i Kafka -----
                ssh $i "/opt/modules/kafka/bin/kafka-server-start.sh -daemon /opt/modules/kafka/config/server.properties"
        done

}
;;
"stop"){
        for i in server1 server2 server3
        do
                echo ----- Stopping $i Kafka -----
                ssh $i "/opt/modules/kafka/bin/kafka-server-stop.sh"
        done

}
;;
esac