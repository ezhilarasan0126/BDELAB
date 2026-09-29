#!/bin/bash
mongod --replSet "rs0" --port 27017 --dbpath ./rs1/db --bind_ip localhost --fork --logpath ./rs1/mongo.log
mongod --replSet "rs0" --port 27018 --dbpath ./rs2/db --bind_ip localhost --fork --logpath ./rs2/mongo.log
mongod --replSet "rs0" --port 27019 --dbpath ./rs3/db --bind_ip localhost --fork --logpath ./rs3/mongo.log
mongo --port 27017 <<EOF
rs.initiate({
  _id: "rs0",
  members: [
    { _id: 0, host: "localhost:27017" },
    { _id: 1, host: "localhost:27018" },
    { _id: 2, host: "localhost:27019" }
  ]
})
EOF