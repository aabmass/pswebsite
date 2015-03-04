PS Website
===============

Dependencies
------------
* Python 3
  Install python dependencies with `pip` (or `pip3` depending on the OS):

  ```bash
  pip3 install --user Flask Flask-Login Flask-SQLAlchemy \
      Flask-User WTForms mysql-connector-python
  ```

* MySQL (or any DBMS supported by Flask-SQLAlchemy -- would require some modifications)

Setup
-------
* You need a database user with all permissions on some database.
  To make a new user (`newuser`, with `password`) and database (`newdb`) in MySQL:
    
  ```SQL
  CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
  CREATE DATABASE newdb;
  GRANT ALL PRIVILEGES ON newdb.* TO 'newuser'@'localhost';
  FLUSH PRIVILEGES;
  ```

* Create a config file.
  There is a shipped sample config file, `config.sample.py`. Copy this file into `psbackend` folder and modify it with your database credentials. Unless you're deploying, you probably want to use the debug environment.

* Create the tables
  Run the script: `./script/createall.py`

* Potential admin creation details here

Run (dev)
------
Just do `./run.py`.
