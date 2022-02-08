arquivo = open('classes_heranca.txt', 'r')


for linha in arquivo:
    linha = linha.strip()
    print(linha)

arquivo.close()