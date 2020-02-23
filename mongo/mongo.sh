#!/usr/bin/env bash

nohup /usr/bin/mongod --bind_ip_all --port $MONGO_PORT &

while [[ $(ps aux | grep [m]ongod | wc -l) -ne 1 ]]; do
    sleep 5
done

while [[ $(mongo --quiet --eval 'JSON.stringify(db.stats())' | jq -r .ok 2> /dev/null) -ne 1 ]]; do
    sleep 5
done

mongo --host 127.0.0.1 --port 27017 "admin" /opt/mongo-init.js
mongo --host 127.0.0.1 --port 27017 "tweets" /opt/mongo-init-tweets.js
