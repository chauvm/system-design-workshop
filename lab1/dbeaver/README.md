# Download
Go to https://dbeaver.io/download/ and choose a DBeaver Community binary.

Upon running DBeaver the first time, it offers a sample SQLite database for exploration. From here, you can browse tables, see their columns, and explore indexes...

Next, try to create a new connection with the `flask-tutorial/tutorial's database.

1. Once you have the flask app running, locate the database file at `lab1/flask-tutorial/tutorial/instance/flaskr.sqlite`
2. From DBeaver's Database Navigator tab on the left, right click > Create > Connection. Select SQLite, and click Open to browse to the `flaskr.sqlite`
3. Hit Finish, the `flaskr.sqlite` should be visible for exploration

You can play with the following operations
- run a SELECT query
- insert a Post
- update a Post
- Create a ERD (Entity Relation Diagrams) to create graphic presentations of database entities and the relations between them (right click on Diagrams at the bottom left, choose Create New ER Diagram, and select Post and User tables)