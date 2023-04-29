from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from settings import Config
from string import ascii_letters, digits


SIZE_SHORT_URL = 16
SYMBOLS_CHOICE = list(ascii_letters + digits)


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import api_views, error_handlers, views, models