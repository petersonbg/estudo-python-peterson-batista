listas_anin = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#print(listas[0][1])
for lista in listas_anin:
    # print(lista)
    for num in lista:
        print(num)

#TABULEIRO
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

#JOGO DA VELHA
print([['X' if num % 2 == 0 else 'O' for num in range(1, 4)]for num in range(1, 4)])