class Cliente:
    contador = 1

    def __init__(self, nome, sobrenome, cpf):
        self.id = Cliente.contador
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        Cliente.contador += 1

    @property
    def retorna_dados(self):
        return f'Id: {self.id}, Nome: {self.__nome} {self.__sobrenome}, Cpf: {self.__cpf}'


nome = input('Nome: ')
sobrenome = input('Sobrenome: ')
cpf = input('Cpf: ')

cliente = Cliente(nome, sobrenome, cpf)

print(cliente.retorna_dados)
print(vars(cliente))


