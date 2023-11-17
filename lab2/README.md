# Overview
In this lab, you will learn to use Datadog to monitor a Postgres database via Datadog's free course https://learn.datadoghq.com/courses/database-monitoring.

You can examine Google's Microservices demo to understand how to deploy a microservice system in a Kubernetes cluster https://github.com/GoogleCloudPlatform/microservices-demo.


# Notes
## Datadog lab
You should go through the first challenge of this lab https://learn.datadoghq.com/courses/database-monitoring to understand at high level how Datadog collects metrics and common database metrics.

Subsequent sections involve adding custom metrics and debugging database issues, which are more advanced and not relevant to System Design interviews.

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

