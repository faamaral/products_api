'''
Descricao :
	Implementação de função para indentificar as chaves no formato json que chegam da requisição
Aluno :
	Fabiano Amaral Alves
Data :
	31 / 07 / 2021
'''
def verify_data(data):
    arg = ['id', 'name', 'description', 'manufacturer', 'price', 'amount']
    i = []
    for d in data.keys():
        for a in arg:
            if d in a:
                i.append(d)
    return len(i)
