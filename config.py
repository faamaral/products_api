import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.flaskenv'))

secret = os.urandom(24)

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or secret
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'products.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False