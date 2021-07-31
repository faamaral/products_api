'''
Descricao :
	Responsavel por criar uma instancia da aplicação
Aluno :
	Fabiano Amaral Alves
Data :
	31 / 07 / 2021
'''

from flask import Flask
from flask_migrate import Migrate

from .database.models import Product, database
from product_api.routes.api_routes import api_bp
from config import Config

migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    database.init_app(app)
    migrate.init_app(app, database)

    app.register_blueprint(api_bp)

    return app