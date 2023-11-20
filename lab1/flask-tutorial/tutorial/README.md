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
