import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# create the application object of class Flask
app = Flask(__name__)

# read and use our config file
app.config.from_object('config')

# initialise our database
db = SQLAlchemy(app)

from app import views, models

