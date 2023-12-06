# Overview
Demo using Celery to improve user experience when filling forms.

Repo: https://github.com/realpython/materials/tree/master/celery-async-tasks


Guide: https://realpython.com/asynchronous-tasks-with-django-and-celery/


(Optional) Celery overview: https://www.vinta.com.br/blog/celery-overview-archtecture-and-how-it-works


In this demo application, users input in a simple form that upon submission, sends an email.

Sending emails is a good example of a long-running process that can be handled asynchronously in the background, without disrupting the user experience while they fill out a form. This approach is commonly used for various tasks, including verifying purchases, detecting fraud, and identifying harmful content.

We have learned in Session 3 of the System Design Workshop that a message queue system is required to act as a temporary buffer to store and distribute asynchronous requests. In this example, we will use Celery to demonstrate:

1) how it receives messages (send email request) from the Django webapp


2) how the messages are stored in a message broker. Here we will use Redis as the message broker for Celery (Celery supports a couple of [brokers](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/index.html)).


3) how Celery workers get started, and execute requests (sending emails)

# Step-by-step instructions
1. Setup
Clone https://github.com/realpython/materials/tree/master/celery-async-tasks.

Create a python virtual environment and install necessary dependencies in `source_code_final`.
```
$ python -m venv venv
$ source venv/bin/activate
(venv) $

(venv) $ python -m pip install django
(venv) $ python -m pip install celery
(venv) $ python -m pip install redis

```

2. Run the synchronous version of form submission
Go back to `source_code_initial` and start the Django webserver.
```
python manage.py migrate  # this command initializes the database

python manage.py runserver  # this command actually starts the Django webapp

```
Navigate to `localhost:8000` and fill in a fake email and a message. You should see the submission takes very long to finish loading and redirecting you to the success page.

This long wait is simulated by `source_code_initial/feedback/forms.py`'s sleep command:
```
class FeedbackForm(forms.Form):
    ...

    def send_email(self):
        """Sends an email when the feedback form has been submitted."""
        sleep(20)  # Simulate expensive operation that freezes Django
        send_mail(
            "Your Feedback",
            f"\t{self.cleaned_data['message']}\n\nThank you!",
            "support@example.com",
            [self.cleaned_data["email"]],
            fail_silently=False,
        )
```

3. Hit Ctrl-C to stop the slow version of the Django webapp
4. Examine the asynchronous version
From now on, go to `source_code_final`.
We'll need to start the following components:
- Redis
- Celery workers
- Django webapp

5. Start a Redis instance
First off, we need to start Celery, which essentially has 2 parts:
- a Redis instance as a message broker as well as the backend to store task results
- a Celery worker (or multiple ones) to process tasks

In this step, let's start the Redis instance first. If you have not yet installed Redis from Lab 2, follow https://redis.io/docs/install/.

```
$ redis-server

97105:C 05 Dec 2023 23:45:10.019 * oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo                             
...
97105:M 05 Dec 2023 23:45:10.020 * Ready to accept connections tcp
```

6. Start a Celery worker
```
python -m celery -A django_celery worker
```
Explanation:
- `-m celery``: This option tells Python to execute the module named celery.
- `-A django_celery``: This option specifies the Celery application to use. In this case, it's django_celery, which is the name of the Django project.
- `worker`: This is the command to start the Celery worker process. You can type `celery worker --help` to see more options with this command, including specifying task queue(s) with -Q, defining scheduled tasks with -s, tuning worker pool with --time-limit and --concurrency... 

7. Submitting an async task
Go to `source_code_final/feedback/forms.py` to see changes made to `send_email`, and follow the `send_feedback_email_task` task definition to confirm that all the code has been moved under it. 

The only difference in `source_code_final` is that we call `send_feedback_email_task.delay()` and provide the function call with necessary parameters. Celery takes care of the rest, e.g. gives this task an ID, write the task into the Redis broker, and let one of Celery workers pick up the task. Once the Celery worker is done processing the task, it updates the task status in the backend database, which is also Redis in this demo.

To illustrate these steps, start the Django webserver, go to `localhost:8000` and submit another form.

```
python manage.py runserver
```

You should see that the form comes back immediately unlike last time.

8. Examine the message broker
Use `redis-cli` to interact with the Redis instance.
```
$ redis-cli

127.0.0.1:6379> KEYS *  # show all keys. WARNING: DO NOT run this command in production as it can return millions of keys!

1) "celery-task-meta-bc31209f-42cc-4839-a685-d17056156fca"

```

Examine this task by getting its value, we can see that the value is actually an object storing the task metadata such as task status.

```
127.0.0.1:6379> GET "celery-task-meta-bc31209f-42cc-4839-a685-d17056156fca"

"{\"status\": \"SUCCESS\", \"result\": null, \"traceback\": null, \"children\": [], \"date_done\": \"2023-12-06T07:49:52.250847\", \"task_id\": \"bc31209f-42cc-4839-a685-d17056156fca\"}"
```

9. Retries, error handling, timeout
When writing code, you should always think of handling failures.
Read [Celery doc](https://docs.celeryq.dev/en/stable/userguide/tasks.html#retrying) to learn about a couple of task options for this purpose:
- `retry a task on specific errors`. This is useful for known transient errors that can be resolved with a retry, e.g. network error.
- `set a max number of retries`. This is so that a task with high failure rate doesn't keep running and consuming worker resources.
- `retry delay, retry backoff`. This helps even out the number of failed tasks being retried.

This [Doordash's Best practice of retry strategy article](https://developer.doordash.com/en-US/docs/drive/reference/retry_pattern/) has a nice overview of DOs and DONTs when using retry.


This is the end of Lab 3. Hit Ctrl-C or `exit` to close running apps.
