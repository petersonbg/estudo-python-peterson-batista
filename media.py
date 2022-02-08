notas = []
for i in range(1, 5):
    notas.append(int(input(f'Digite a nota {i}: ')))

soma_notas = sum(notas)
media = soma_notas / 4

print(f'Sua média foi {media}')
