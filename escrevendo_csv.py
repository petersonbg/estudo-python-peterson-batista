"""
from csv import writer

with open('filmes.csv', 'w', encoding="utf8") as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Titulo', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Digite o nome do filme: ')
        if filme != 'sair':
            genero = input('Digite o gênero: ')
            duracao = input('Digite a duração: ')
            escritor_csv.writerow([filme, genero, duracao])
"""
from csv import DictWriter

with open('musica.csv', 'w', encoding="utf8") as arquivo:
    cabecalho = ['Titulo', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    musica=None
    while musica != 'sair':
        musica = input('Digite o nome da música: ')
        if musica != 'sair':
            genero = input('Digite o gênero: ')
            duracao = input('Digite a duração: ')
            escritor_csv.writerow({"Titulo": musica, "Gênero": genero, "Duração": duracao})


