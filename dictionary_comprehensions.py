numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

res = {chave: valor * 2 for chave, valor in numeros.items()}
print(res)

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

dicionario = {chaves[i]: valores[i] for i in range(len(chaves))}
print(dicionario)
