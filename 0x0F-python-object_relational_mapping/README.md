# README.md - SQLAlchemy ORM Project

![SQLAlchemy Logo](https://www.sqlalchemy.org/img/sqla_logo.png)

**Project Information**

- Project: 0x0F. Python - Object-relational mapping
- Technologies: Python, SQLAlchemy, MySQL

**Before You Start...**

Please make sure your MySQL server is in version 8.0. You can follow these steps to install MySQL 8.0 in Ubuntu 20.04:

```bash
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info
(2, 0, 3, 'final', 0)
$ sudo pip3 install SQLAlchemy
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__
'1.4.22'
```

**Project Overview**

This project focuses on Object-Relational Mapping (ORM) using SQLAlchemy, a powerful library that bridges the gap between Python and databases. In this project, you will work with MySQL databases and perform various tasks using SQLAlchemy. The project is divided into multiple tasks, each building on the previous one.

**Project Tasks**

1. **Get all states**: Write a script to list all states from the database.

2. **Filter states**: Write a script to list states with names starting with 'N'.

3. **Filter states by user input**: Write a script to filter states by user input.

4. **SQL Injection...**: Secure a script from SQL injection while filtering states.

5. **Cities by states**: List all cities from the database.

6. **First state model**: Create a State class and an instance of Base for ORM.

7. **All states via SQLAlchemy**: List all State objects from the database.

8. **First state**: Print the first State object from the database.

9. **Contains `a`**: List all State objects containing the letter 'a'.

10. **Get a state**: Print the State object with a given name.

11. **Add a new state**: Add a new State object to the database.

12. **Update a state**: Change the name of a State object.

13. **Delete states**: Delete all State objects with names containing the letter 'a'.

**Learning Objectives**

By completing this project, you will achieve the following learning objectives:

- Gain proficiency in using SQLAlchemy for database interaction.
- Learn how to create and manipulate database tables.
- Develop skills in querying and modifying data using ORM.
- Understand how to handle user input and prevent SQL injection.

**Requirements**

-  vi, vim, emacs.
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).
- Your files will be executed with MySQLdb version 2.0.x.
- Your files will be executed with SQLAlchemy version 1.4.x.
- Ensure all your files end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/python3`.
**Install and Activate a Virtual Environment**

To create a Python Virtual Environment, allowing you to install specific dependencies for this Python project, follow these steps:

```bash
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
```
