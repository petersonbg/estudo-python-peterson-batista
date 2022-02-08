# Atributos Publicos
class ContaCorrente:
    contador = 5000

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        Produto.contador = self.id

    def imprime_produto(self):
        return f'ID: {self.id} - Produto: {self.nome} - Descrição: {self.descricao} - Valor: R${self.valor}'


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

# Atrinutos Privados

class Acesso:

    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha


user1 = Usuario('Peterson', 'Batista', 'petersonbatista8@gmail.com', '12345')
produto1 = Produto('Arroz', 'Marca 1', 17.99)

print(user1.nome_completo())

print(produto1.imprime_produto())






