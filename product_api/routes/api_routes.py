'''
Descricao :
	Responsavel por definir as rotas e CRUD da api
Aluno :
	Fabiano Amaral Alves
Data :
	31 / 07 / 2021
'''
import json

from flask import Blueprint, request
from flask_restful import Resource, Api

from product_api.database.models import Product, database
from product_api.utils import methods

api_bp = Blueprint('api', __name__)
api = Api(api_bp)



class ListProduct(Resource):
    def get(self):
        products = Product.query.all()
        return [Product.serialize(product) for product in products]
    
    def post(self):
        data = json.loads(request.data)
        # Gambiarra para validar os atributos da requisição
        i = methods.verify_data(data)

        if i != 5:
            return {
                'status': 400,
                'mensagem': 'Não foi possivel adicionar o produto, por favor não coloque o id no corpo da requisição'
            }
        #fim da gambiarra

        product = Product(
            name=data['name'],
            description=data['description'],
            manufacturer=data['manufacturer'],
            price=data['price'],
            amount=data['amount']
        )
        database.session.add(product)
        database.session.commit()
        return Product.serialize(product), 201

class Products(Resource):
    def get(self, id):
        product = Product.query.filter_by(id=id).first_or_404()
        return Product.serialize(product)

    def put(self, id):
        data = json.loads(request.data)
        # Inicio da gambiarra
        i = methods.verify_data(data)
        if i != 5:
            return {
                'status': 400,
                'mensagem': 'Não foi possivel editar o produto, por favor não adicione o id no corpo da requisição'
            }
        #fim da gambiarra
        product = Product.query.filter_by(id=id).first_or_404()
        product.name=data['name']
        product.description=data['description']
        product.manufacturer=data['manufacturer']
        product.price=data['price']
        product.amount=data['amount']

        database.session.add(product)
        database.session.commit()

        return Product.serialize(product), 201

    def delete(self,id):
        product = Product.query.filter_by(id=id).first_or_404(description=f'ID={id} não foi encontrado')
        database.session.delete(product)
        database.session.commit()
        return {
            'status':200,
            'mensagem': 'Produto deletado com sucesso'
        }

api.add_resource(ListProduct, '/', '/product', '/product/')
api.add_resource(Products, '/product/<int:id>')
        


