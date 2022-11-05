saldo = 0
confirmacao = 1
cont_saque = 0
cont_deposito = 0
extrato = {}

while confirmacao == 1:

    print("""*************MENU**************
    1 - DEPOSITAR
    2 - SACAR
    3 - EXTRATO
    4 - SAIR """)
    operacao = int(input("Insira o tipo de operação que deseja realizar: "))

    if operacao == 1:
        cont_deposito = cont_deposito + 1
        deposito = float(input("Insira o valor do depósito: "))
        if deposito > 0:
            print(f"O valor do depósito foi de R${deposito:.2f}")
            saldo += deposito
            print(f"Saldo Atual: R$ {saldo:.2f}")
            extrato.update({f"Deposito {cont_deposito}": deposito})
        elif deposito <= 0:
            print("\n"
                  "******Favor Inserir Valores Positivos!******\n")

        confirmacao = int(input("Deseja fazer outra operação? (1 - Sim / 2 - Não) "))

    if operacao == 2:

        while cont_saque < 3:
            saque = float(input("Insira o valor do saque: "))
            while saque > saldo:
                print("Saldo insuficiente!")
                break
            if saque > 500:
                print("Valor limite de saque excedido!!")

            elif saque <= saldo:
                saldo -= saque
                cont_saque = cont_saque + 1
                print("Saque realizado com sucesso!")
                print(f"Saldo atual: R$ {saldo:.2f}")
                extrato.update({f"Saque {cont_saque}": saque})

            break
        else:
            print("Numero máximo de operaçoes para saque atingida.")

        confirmacao = int(input("Deseja fazer outra operação? (1 - Sim / 2 - Não) "))

    if operacao == 3:
        print("******* Extrato da Conta ******** ")
        for chave, valor in extrato.items():
            print(chave, f"- R$ {valor:.2f}")

        print(f"\nSaldo Atual: R$ {saldo:.2f}")
        print("********************************* ")

        confirmacao = int(input("Deseja fazer outra operação? (1 - Sim / 2 - Não) "))

    if operacao == 4:
        print("Obrigado! Volte Sempre...")
        break

else:
    print("Obrigado! Volte Sempre...")
