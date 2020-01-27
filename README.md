# FlaskApp

 Using a Tutorial by Miguel Grinberg [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

## Motivation

I spend a majority of my time on **Data Science** related tasks using Python with Jupyter Notebooks, Machine Learning packages and the classic [Numpy](https://numpy.org) and [Pandas](https://pandas.pydata.org).  Since I don't have a lot of experience (or need) for web application building I thought I would work through building one leveraging Flask. A very popular Python framework for building web applications.

## Some Useful Commands

 * Run the application with `flask run`.
 * This will be served up locally at `http://127.0.0.1:5000/`.
 * `CTRL+C` to kill the web server.
 * You can run a dummy local test SMTP server with the following command `python -m smtpd -n -c DebuggingServer localhost:8025`.  _Note: You will need to make sure the MAIL_SERVER and MAIL_PORT environment variables are set_

## Dependencies

* Flask - `pip install flask`
* Python .ENV - `pip install python-dotenv`
* Flask WTForms - `pip install flask-wtf`
* Flask-SQLAlchemy - `pip install flask-sqlalchemy`
* Flast-Migrate - `pip install flask-migrate`
* Flask-Login - `pip install flask-login`
* Flask Mail - `pip install flask-mail`
* Python Java Web Tokens - `pip install pyjwt`
* Bootstrap - `pip install flask-bootstrap`

## What is Flask?

From [The Pallets Projects](https://palletsprojects.com/p/flask/), Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around [Werkzeug](https://palletsprojects.com/p/werkzeug/) and [Jinja](https://palletsprojects.com/p/jinja/) and has become one of the most popular Python web application frameworks.  
