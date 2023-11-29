# Overview
In this lab, you will
- examine Cisco's Microservices demo to understand how to deploy a microservice system in a Kubernetes cluster
- take Datadog's free course https://learn.datadoghq.com/courses/database-monitoring to see how to use Datadog to monitor a Postgres database
- (optional) play with a Flask/Redis application to get familiar with Redis

# Instructions
## Docker Desktop
Follow README.md under `microservice-demo/docker` to install Docker Desktop application if not yet available in your computer and turn on configurations to run a dev Kubernetes cluster.

## (Optional) Redis walkthrough
See `redis/` if you want to try using Redis.

## Kubernetes add-ons
1. Install kubectl to interact with Kubernetes
https://kubernetes.io/docs/tasks/tools/
2. Install Helm to easily create Kubernetes resources
https://helm.sh/docs/intro/install/

At the end, you should have the following tools
```
which kubectl
which helm
```
and Docker Desktop has Kubernetes enabled

## Run microservice demo
We'll follow instructions from https://github.com/cisco-open/martian-bank-demo to run a demo app as described in https://techblog.cisco.com/blog/martianbank-a-microservice-demo-application-for-cloud-native-products.

1. Clone the repo
```
git clone https://github.com/cisco-open/martian-bank-demo.git
cd martian-bank-demo
```
2. Use Helm to install the demo app
```
helm install martianbank martianbank

---
NAME: martianbank
LAST DEPLOYED: Mon Nov 27 14:53:44 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
Installation is successful.
```
From Docker Desktop > Containers, you can see all running containers from this app.

You can also see all Kubernetes pods with
```
kubectl get pods

---
NAME                                  READY   STATUS              RESTARTS   AGE
accounts-5f5b97d4f5-jmhw4             1/1     Running             0          5m27s
atm-locator-57dfdf4ff7-m9lvf          0/1     
...
```

... and view Kubernetes services with
```
kubectl get service
NAME            TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
dashboard       LoadBalancer   10.101.130.119   <pending>     5000:31146/TCP   7m12s
mongodb         ClusterIP      10.104.106.235   <none>        27017/TCP        7m12s
nginx           LoadBalancer   10.98.233.111    localhost     8080:30752/TCP   7m12s
...
```

It may take a couple of minutes for all pods to be up and running without Error status. After all pods are up, you can access the app at http://localhost:8080 (nginx service).

## Examine the demo app
- Look at the architecture diagram to understand the app topology: https://techblog.cisco.com/blog/martianbank-a-microservice-demo-application-for-cloud-native-products
- Look at `nginx/default.conf` to understand some routing rules
- Tail logs from a pod with `kubectl logs -f <pod-name>` and click around to see HTTP logs
- Run `helm uninstall martianbank` to uninstall resources, and play with different configs such as `helm install martianbank martianbank --set SERVICE_PROTOCOL=grpc` to change the communication protocol among dashboard services to gRPC
- Look at protobuf definition under `protobufs/`


## Datadog lab
You should go through the first challenge of this lab https://learn.datadoghq.com/courses/database-monitoring to understand at high level how Datadog collects metrics and common database metrics.

Subsequent sections involve adding custom metrics and debugging database issues, which are more advanced and not relevant to System Design interviews.

Some notes when going through the first challenge:

### Important Database metrics
Summary of https://www.loggly.com/blog/5-ways-to-proactively-monitor-database-performance/
1. Monitor Availability and Resource Consumption
- Availability: database connection, number of healthy nodes
- Resource Consumption: CPI, memory, disk, network
2. Measure and Compare Throughput
- number of transactions/second
- replication latency
- ...
3. Monitor Expensive Queries
Common reasons for slow queries:
- complex queries
- lack indexes
- deadlock
- code changes that allow infite writes
Common solutions:
- use query analysis tools to identify and improve complex queries
- add indexes to commonly queried data, also audit bloated indexes that have frequent updates
- reduce diskspace space: delete unused large tables that take up disk space, delete tombstone records
- close orphan database connections

### echo -e
The `docker exec` command prints out `Postgres connection - OK` in green if it can establish a connection with the Postgres database, and prints out `Cannot connect to Postgres` in red if it can't.

```
docker exec lab-postgres-1 psql -h postgres -U datadog postgres -c \
"select * from pg_stat_database LIMIT(1);" \
&& echo -e "\e[0;32mPostgres connection - OK\e[0m" \
|| echo -e "\e[0;31mCannot connect to Postgres\e[0m"
```

The `echo -e` command is a command used in Linux and Unix-based operating systems to display text on the terminal. The `-e` option enables the interpretation of backslash escapes in the text. It allows you to include special characters and formatting options in the output.

For example, with `echo -e`, you can use escape sequences like `\n` for a new line, `\t` for a tab, or `\b` for a backspace. Here's an example:

```
echo -e "Hello\tWorld!\nThis is a new line."
```

Output:
```
Hello    World!
This is a new line.
```

In this example, the `\t` escape sequence inserts a tab between "Hello" and "World!", and the `\n` escape sequence starts a new line after "World!".


### Docker compose
Docker Compose is a tool that allows you to define and manage multi-container Docker applications. It is a command-line tool that simplifies the process of running and connecting multiple Docker containers as a single application stack.

With Docker Compose, you can define your application's services, networks, and volumes in a YAML file called docker-compose.yml.

See https://docs.docker.com/compose/gettingstarted/.

