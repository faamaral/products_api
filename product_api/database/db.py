from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

database = SQLAlchemy()
migrate = Migrate()

def init_app(app):
    database.init_app(app)
    migrate.init_app(app, database)