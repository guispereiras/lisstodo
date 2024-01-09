from dynaconf import FlaskDynaconf
from flask import Flask
from lisstodo.ext import configuration
from lisstodo.blueprints import views


app = Flask(__name__)

configuration.init_app(app)
views.init_app(app)
