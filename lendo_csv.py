"""
# Possivel de se trabalhar, mão não o recomendado

with open('lutadores.csv', encoding="utf8") as arquivo:
    dados = arquivo.read()
    dados = dados.split(',')
    print(dados)

from csv import reader

with open('lutadores.csv', encoding='utf8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)
    for linha in leitor_csv:
        print(f"Nome: {linha[0]}, Pais: {linha[1]}, Altura: {linha[2]}cm")

"""

from csv import DictReader

with open('lutadores.csv', encoding='utf8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        print(f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']}cm")

