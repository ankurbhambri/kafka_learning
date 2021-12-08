# Kafka Confluent Connect Standalone with Mysql DB

1. Download mysql jdbc jar. <br />
2. Run Zookeeper and Kafka Cluster Server. <br />
3. kafka folder connect standalone properties provide jdbc jar plugin files path avaliable in connectors folders both needed. <br />
4. Another file having mysql properties in which mysql db properties. <br />
5. Then Run connect-standalone.sh connect-standalone.properties mysql.properties written below. <br />
    * Name of Api we can see at http://localhost:8083/connectors/ Mysql-Connect will be shown there
    name=Mysql-Connect <br />
    tasks.max=1 <br />
    connector.class=io.confluent.connect.jdbc.JdbcSourceConnector <br />
    connection.url=jdbc:mysql://localhost:3306/test <br />
    connection.user=root <br />
    connection.password= <br />
    mode=incrementing <br />
    * Auto increment field of table pass here <br />
    incrementing.column.name=id <br />
    table.whitelist=tbl, <br />
    * Topic name like 'test' and mysql table name 'tbl' = test_tbl but we only pass test_. <br />
    topic.prefix=test_ <br />
    poll.interval.ms=100 <br />

6. kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test_tbl ( extra to include --from-beginning)
# Python with kafka dependencies

confluent-kafka==1.4.2 <br />
kafka-python==2.0.1



