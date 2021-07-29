import os
from dotenv import load_dotenv

secret = os.urandom(24)

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or key
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'products.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False