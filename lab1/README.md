# Overview
In this lab, you will create a sample webapp using Flask - a lightweight and flexible web framework for Python.

We will use Postman to make API requests to the webapp to create and view objects. Objects will be stored in a SQLite database.

Finally, we will demonstrate how to use DBeaver, a database management tool, to interact with the SQLite database.

# Installation
## Softwares
See `postman/` and `dbeaver/` for instructions to install Postman and DBeaver.

Meanwhile, go to `flask-tutorial/tutorial`, follow the instructions to create a virtual environment and install flask, and start the webapp.

With the app up and running, which writes data into `lab1/flask-tutorial/tutorial/instance/flaskr.sqlite` - a local file representing a SQLite database, we can use DBeaver to examine the database.

Next steps
1. Follow instructions under `dbeaver/` to connect to the database and perform some operations
2. Follow instructions under `postman/` to make a few POST requests that will create and store classroom objects in a SQLite database

