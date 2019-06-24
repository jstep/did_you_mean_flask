from flask import Flask
from flask_caching import Cache
from flask_bootstrap import Bootstrap
from config import Config
 
app = Flask(__name__)
app.config.from_object(Config)

cache = Cache(app)

bootstrap = Bootstrap(app)

from app import routes, errors

