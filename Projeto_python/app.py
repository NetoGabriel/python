# from datetime import datetime

# postagem = datetime.strptime(input('Digite a data da postagem (dd/mm/aaaa): '), '%d/%m/%Y')
# print(type(postagem))

# data_inicio = datetime.now()
# data_entrega = postagem

# tempo = data_inicio - data_entrega
# print(f'Tempo restante para a entrega: {tempo}')

listagem = ['fone', 'celular', 'computador', 'nn', 'e']

for listagem in listagem:
    print(listagem)
    if listagem == 'e':
        break
    