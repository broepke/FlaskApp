# FlaskApp

 Using a Tutorial by Miguel Grinberg [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

## Motivation

I spend a majority of my time on **Data Science** related tasks using Python with Jupyter Notebooks, Machine Learning packages and the classic [Numpy](https://numpy.org) and [Pandas](https://pandas.pydata.org).  Since I don't have a lot of experience (or need) for web application building I thought I would work through building one leveraging Flask. A very popular Python framework for building web applications.

## Some Useful Commands

 * Run the application with `flask run`.
 * This will be served up locally at `http://127.0.0.1:5000/`.
 * `CTRL+C` to kill the web server.
 * This is predicated by having an environment variable set to `FLASK_APP=microblog.py`.  This is done via the `.flaskenv` file in the root directory and set via the Python `python-dotenv` package. (Nothing needed after that's set).

## Dependencies

* Flask - `pip install flask`
* Python .ENV - `pip install python-dotenv`
* Flask WTForms - `pip install flask-wtf`
* Flask-SQLAlchemy - `pip install flask-sqlalchemy`
* Flast-Migrate - `pip install flask-migrate`

## What is Flask?

From [The Pallets Projects](https://palletsprojects.com/p/flask/), Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around [Werkzeug](https://palletsprojects.com/p/werkzeug/) and [Jinja](https://palletsprojects.com/p/jinja/) and has become one of the most popular Python web application frameworks.  
