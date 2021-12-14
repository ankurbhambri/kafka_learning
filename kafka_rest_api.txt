# 1) Get Worker information
curl -s localhost/ | jq
# 2) List Connectors available on a Worker
curl -s localhost/connector-plugins | jq
# 3) Ask about Active Connectors
curl -s localhost/connectors | jq
# 4) Get information about a Connector Tasks and Config
curl -s localhost/connectors/source-twitter-distributed/tasks | jq
# 5) Get Connector Status
curl -s localhost/connectors/file-stream-demo-distributed/status | jq
# 6) Pause / Resume a Connector (no response if the call is succesful)
curl -s -X PUT localhost/connectors/file-stream-demo-distributed/pause
curl -s -X PUT localhost/connectors/file-stream-demo-distributed/resume
# 7) Get Connector Configuration
curl -s localhost/connectors/file-stream-demo-distributed | jq
# 8) Delete our Connector
curl -s -X DELETE localhost/connectors/file-stream-demo-distributed
# 9) Create a new Connector
curl -s -X POST -H "Content-Type: application/json" --data '{"name": "file-stream-demo-distributed", "config":{"connector.class":"org.apache.kafka.connect.file.FileStreamSourceConnector","key.converter.schemas.enable":"true","file":"demo-file.txt","tasks.max":"1","value.converter.schemas.enable":"true","name":"file-stream-demo-distributed","topic":"demo-2-distributed","value.converter":"org.apache.kafka.connect.json.JsonConverter","key.converter":"org.apache.kafka.connect.json.JsonConverter"}}' http://localhost/connectors | jq
# 10) Update Connector configuration
curl -s -X PUT -H "Content-Type: application/json" --data '{"connector.class":"org.apache.kafka.connect.file.FileStreamSourceConnector","key.converter.schemas.enable":"true","file":"demo-file.txt","tasks.max":"2","value.converter.schemas.enable":"true","name":"file-stream-demo-distributed","topic":"demo-2-distributed","value.converter":"org.apache.kafka.connect.json.JsonConverter","key.converter":"org.apache.kafka.connect.json.JsonConverter"}' localhost/connectors/file-stream-demo-distributed/config | jq
