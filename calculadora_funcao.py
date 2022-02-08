while True:
    try:
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
    except ValueError as a:
        print('Valor não aceito! Tente novamente.')
        print(a)
    else:
        break

operacao = input(
            "\nESCOLHA A OPERAÇÃO:\n\"a\" para adição\n\"s\" para subtração\n"
            "\"m\" para multiplicação\n\"d\" para divisão\nDigite a escolha: ")


def soma():
    return num1 + num2


def subtracao():
    return num1 - num2


def multiplica():
    return num1 * num2


def divisao():
    return num1 / num2


if operacao == 'a':
    print('Resultado da adição: ', soma())

if operacao == 's':
    print('Resultado da subtração: ', subtracao())

if operacao == 'm':
    print('Resultado da multiplicação: ', multiplica())

if operacao == 'd':
    print('Resultado da divisão: ', divisao())
