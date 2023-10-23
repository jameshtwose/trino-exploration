# Trino server setup
- `docker run -p 8080:8080 --name trino trinodb/trino`
- `docker exec -it trino bash`
- copy paste the files in `example_configuration` to the trino container
<!-- - `docker cp ./example_configuration/ trino:/etc/trino/` -->
- `docker cp ./example_configuration/catalog/kafka.properties trino:/etc/trino/catalog/kafka.properties`
- `docker cp ./example_configuration/catalog/mysql.properties trino:/etc/trino/catalog/mysql.properties`

# Trino cli setup
- `docker run -it --rm --network host trinodb/trino:latest trino --server localhost:8080`
- `show catalogs;`
- `show schemas in kafka;`

# Kafka setup
- `docker-compose up -d`
- `docker exec -it trino-exploration-kafka-1 bash` - enter the kafka container
- `cd /opt/bitnami/kafka/bin`
- `kafka-topics.sh --create --topic ppeAvailabilityHospitalC --bootstrap-server localhost:9093`
- `docker cp ./data/Kafka_Dataset.json trino-exploration-kafka-1:/opt/bitnami/kafka/bin/Kafka_Dataset.json` - copy the dataset to the kafka container (this is a one time step - in a different terminal)
- `cat Kafka_Dataset.json | kafka-console-producer.sh --topic ppeAvailabilityHospitalC --bootstrap-server localhost:9093`
- `kafka-console-consumer.sh --topic ppeAvailabilityHospitalC --from-beginning --bootstrap-server localhost:9092` - check if the data is in the topic

# MySQL setup
- `docker run --name mysql-db -e MYSQL_ROOT_PASSWORD=mypassword -d mysql:latest`
- `docker ps` - check if the container is running
- `docker inspect mysql-db | grep -i IPAddress` - get the ip address of the container