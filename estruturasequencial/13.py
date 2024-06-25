form = 0
sexo = str(input("Digite M para sexo masculino e F para sexo feminino: "))
h = float(input("Digite sua altura em metros(.): "))


if sexo == 'M':
    form = (72.7*h) - 58
elif sexo == 'F':
    form = (62.1*h) - 44.7

print(f"Seu peso ideal seria de {form} kg, tendo vista que você é do sexo {sexo}")