# Flask
from flask import Flask
app = Flask(__name__)
app.config.from_object('config')

# SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

from app import views, models