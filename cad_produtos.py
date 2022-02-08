# Adicionando valores de inputs em dicionarios
recebe_produto = []
recebe_valor = []


while True:
    recebe_produto.append(str(input('Produto: ')))
    recebe_valor.append(float(input('Valor: ')))
    recebe_listas = dict(zip(recebe_produto, recebe_valor))
    print('\n1 - Sim\n2 - Não')
    opcao = int(input('Deseja cadastrar outro produto? '))
    if opcao == 1:
        continue
    else:
        break

for chave, valor in recebe_listas.items():
    print(f'{chave} - {valor}')


