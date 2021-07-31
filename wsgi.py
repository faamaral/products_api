'''
Descricao :
	Responsavel por executar a aplicação num servidor gunicorn
Aluno :
	Fabiano Amaral Alves
Data :
	31 / 07 / 2021
'''
from product_api.app import create_app

app = create_app()