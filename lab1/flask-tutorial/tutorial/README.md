Follow the instructions in https://github.com/pallets/flask/tree/main/examples/tutorial/README.rst to start the tutorial app.
The application should be available at http://127.0.0.1:5000/.


For Mac users, the process looks something like this:

```

Create a virtualenv and activate it::

    (tutorial) $ python3 -m venv .venv
    (tutorial) $ . .venv/bin/activate

Install Flaskr::

    $ pip install -e .

Run the app::

    $ flask --app flaskr init-db
    $ flask --app flaskr run --debug
```

Open http://127.0.0.1:5000 in a browser, you should see the sample app.


## (Optional) gunicorn to run multiple webapp processes
See https://flask.palletsprojects.com/en/3.0.x/deploying/gunicorn/ for what gunicorn is.
Basically, it allows you to run multiple instances of you application in parallel. This is great in production because we can take advantages of multi-core servers.

```

Stop the running app, and install guinicorn::

$ pip install gunicorn


Start the flaskr app with gunicorn, here we use 4 workers
(tutorial) $ gunicorn -w 4 'flaskr:create_app()'

You can see from the console that 4 new processes are starting.

[2023-11-20 15:36:33 -0800] [12900] [INFO] Starting gunicorn 21.2.0
[2023-11-20 15:36:33 -0800] [12900] [INFO] Listening at: http://127.0.0.1:8000 (12900)
[2023-11-20 15:36:33 -0800] [12900] [INFO] Using worker: sync
[2023-11-20 15:36:33 -0800] [12901] [INFO] Booting worker with pid: 12901
[2023-11-20 15:36:33 -0800] [12902] [INFO] Booting worker with pid: 12902
[2023-11-20 15:36:33 -0800] [12903] [INFO] Booting worker with pid: 12903
[2023-11-20 15:36:33 -0800] [12904] [INFO] Booting worker with pid: 12904
[2023-11-20 15:37:52 -0800] [12900] [INFO] Handling signal: winch

```
Going to http://127.0.0.1:8000/, you should see the same application.