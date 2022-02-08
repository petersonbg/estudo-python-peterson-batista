arquivo = open('classes_heranca.txt', 'a')


class Funcionario:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    @property
    def get_nomecompleto(self):
        return f'Nome: {self.__nome} {self.__sobrenome}, Cpf: {self.__cpf}'


class Vendedor(Funcionario):
    def __init__(self, nome, sobrenome, cpf, usuario, senha):
        super().__init__(nome, sobrenome, cpf)
        self.__usuario = usuario
        self.__senha = senha

    @property
    def get_nomecompleto(self):
        return super().get_nomecompleto + f', Usuario: {self.__usuario}, Senha: {self.__senha}\n'


while True:
    nome = input('Nome: ')
    sobrenome = input('Sobrenome: ')
    cpf = input('Cpf: ')
    usuario = input('Usuario: ')
    senha = input('Senha: ')

    funcionario = Vendedor(nome, sobrenome, cpf, usuario, senha)

    arquivo.write(funcionario.get_nomecompleto)

    print('1 - Sim\n2 - Não')
    opcao = input('Deseja cadastrar outro Vendedor? ')

    if opcao == '1':
        continue
    else:
        break

arquivo.close()
