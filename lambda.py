nome_completo = lambda recebe_nome, recebe_sobrenome: recebe_nome.strip().title() + ' ' + recebe_sobrenome.strip().title()

recebe_nome = input('Digite o nome: ')
recebe_sobrenome = input('Digite o sobrenome: ')

print(nome_completo(recebe_nome, recebe_sobrenome))


