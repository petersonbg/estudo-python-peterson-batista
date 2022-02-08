pag_hora = float(input('Quanto ganha por hora: '))
horas_trab = int(input('Quantas horas trabalhou no mês: '))

salario_bruto = horas_trab * pag_hora
imp_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
descontos = imp_renda + inss + sindicato
salario_liq = salario_bruto - descontos


print(f'+ Salario Bruto: R${salario_bruto}')
print(f'- Imposto de renda: R${imp_renda}')
print(f'- INSS: R${inss}')
print(f'- Sindicato: R${sindicato}')
print(f'= Salario Liquido: R${salario_liq}')