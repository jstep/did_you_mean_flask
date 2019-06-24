import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'total-secret'

    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 600
