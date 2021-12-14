# Kafka Setup

* Download https://kafka.apache.org/downloads latest scala version <br />

* Extract tar -xvf kafka package <br />

* Set Path export PATH=/home/ubuntu/kafka_2.13-2.8.0/bin:$PATH <br />

* Create data folder in kafka_* directort <br />

* Then create two folder and zookeeper and kafka <br />

* Suggestion !! Edit zookeeper.properties and kafka.properties files already present in Config folder 
    - (log.dirs=/home/ubuntu/kafka_2.13-2.8.0/data/kafka) and <br />
    - (log.dirs=/home/ubuntu/kafka_2.13-2.8.0/data/zookeeper) <br /> 
    - Reason of these changes is kafka by default creates logs of kafka and zookeeper configuration in tmp directory which is created in volatile memory and there is chance of data lost thats why my suggestion is to change path <br />

# Basic commands present in kafka_basic_commands.txt

# Useful Jars for Examples are in connector_jars
   - Provide plugins path in Worker.properties for JDBC connect <br /> 
   - Paste in any of the given director paths for better reach plugin.path=/usr/local/share/java,/usr/local/share/kafka/plugins,/opt/connectors, <br /> 

# Kafka Connect Distributed and Standalone with Mysql DB and File with Examples given in folder 

* kafka-standalone-example - Standalone mode is typically used for development and testing, or for lightweight, single-agent environments (for example, sending web server logs to Kafka). <br />

- connect-standalone.sh workers.properties A_Source.properties and A_Sink.properties <br /> 

* kafka-distributed-example - Kafka Connect distributes running connectors across the cluster. You can add more nodes or remove nodes as your needs evolve. Distributed mode is also more fault tolerant. If a node unexpectedly leaves the cluster, Kafka Connect automatically distributes the work of that node to other nodes in the cluster. <br /> 

- connect-distributed.sh worker.properties <br />  

- ex - Then Run Connectors configs writen in json <br /> 

# Note: 
* While sink in any mode sink automatically created by kafka just need to define the name (for ex- In Mysql JDBC connect we only need to provide topics='xyz' this will automaticaly created in Mysql Table and in File sink same file will be created automatically.)
* While Source Topic and file must be present and defined in configurations 

# Python with kafka dependencies

confluent-kafka==1.4.2 <br />
kafka-python==2.0.1



