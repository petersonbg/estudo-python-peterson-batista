aluno_notas = {'Peterson': [5.0, 2.1], 'Paulo': [7.8, 6.2], 'Marcia': [8.2, 9.3], 'José': [3.1, 9.8], 'Ana': [9.2, 7.8]}
media = []

for chave, valor in aluno_notas.items():
    media = sum(valor) / len(valor)
    valor.append(media)

aprovados = {chave: valor for chave, valor in aluno_notas.items() if not valor[2] < 7.0}


print(aluno_notas)
print(aprovados)
