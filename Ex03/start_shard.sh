#!/bin/bash
mongod --configsvr --replSet configReplSet --port 26050 --dbpath ./config/db --bind_ip localhost --fork --logpath ./config/config.log
mongod --shardsvr --port 27020 --dbpath ./shard1/db --bind_ip localhost --fork --logpath ./shard1/mongo.log
mongod --shardsvr --port 27021 --dbpath ./shard2/db --bind_ip localhost --fork --logpath ./shard2/mongo.log
mongos --configdb configReplSet/localhost:26050 --bind_ip localhost --fork --logpath mongos.log --port 27017
mongo --port 27017 <<EOF
sh.addShard("localhost:27020")
sh.addShard("localhost:27021")
sh.enableSharding("college")
sh.shardCollection("college.students", { "rollno": 1 })
EOF
