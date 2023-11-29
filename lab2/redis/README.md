Let's learn Redis.
# Overview
Redis = Remote Dictionary Service
- What: a database, specifically a key value store
- Usage: a database, a cache, or a message broker
- Properties: fast, scalable, with optional durability

## How
Redis stores data as strings in RAM with an option to write states into HDD for durability. It supports a couple of data structures: sets, sorted sets, bitmaps... Redis is designed to be easily scalable, by adding more nodes and supporting data sharding across nodes.

## Common use cases
... and popular interview questions:
- Modern gaming experiences: real-time leaderboard
- Session store
- Chat, messaging, and queues
See https://redis.com/blog/5-industry-use-cases-for-redis-developers/

# Learn
## Installation
https://redis.io/docs/install/

## Start a redis instance
Clone this repo https://github.com/docker/awesome-compose/tree/master/flask-redis

Use Docker Compose to start the application
```
(flask-redis) $ docker compose up -d

---
It will take a while to download Docker images
```
We can then use `docker ps` to see running containers.

```
docker ps
CONTAINER ID   IMAGE                COMMAND                  CREATED         STATUS         PORTS                    NAMES
da9b9ec532cd   flask-redis-web      "python3 app.py"         8 seconds ago   Up 8 seconds   0.0.0.0:8000->8000/tcp   flask-redis-web-1
bd9b924a8308   redislabs/redismod   "redis-server --load…"   9 seconds ago   Up 8 seconds   0.0.0.0:6379->6379/tcp   flask-redis-redis-1
```

The Redis instance to running in port 6379.

Use `redis-cli` to ping, or access its data as shown in the repo's README.md
```
# ping to check connection
$ redis-cli -h 0.0.0.0 -p 6379 PING
PONG

# access the Redis instance and tail its activity logs
$ redis-cli -h 0.0.0.0 -p 6379     
0.0.0.0:6379> monitor
OK
1701220745.120744 [0 172.18.0.3:41546] "INCRBY" "hits" "1"
1701220745.123110 [0 172.18.0.3:41546] "GET" "hits"

# we can increment the key "hits" from Redis console
0.0.0.0:6379> GET hits
"1"
0.0.0.0:6379> INCR hits
(integer) 2
0.0.0.0:6379> GET hits
"2"
```



