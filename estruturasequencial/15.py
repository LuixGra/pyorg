shora = float(input("Quanto você ganha por hora?: "))
thora = float(input("Quantas horas você trabalhou esse mês?: "))

salario = shora * thora
ir = salario * (11/100)
inss = salario * (8/100)
sindicato = salario * (5/100)

salario_liquido = salario - (ir + inss + sindicato)

print(f"+ Salario bruto: {salario}R$\n- IR: {ir}R$\n- INSS: {inss}R$\n- Sindicato: {sindicato}R$\n= Salario Líquido: {salario_liquido}R$")