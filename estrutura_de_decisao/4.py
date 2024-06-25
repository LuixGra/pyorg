vogais = ['a', 'e', 'i', 'o', 'u']
letra = str(input("Digite uma letra.(minuscula)\n"))

contador = 0

for vogal in vogais:
    if letra == vogal:
        contador += 1

if contador == 0:
    print(f"A letra {letra} é uma consoante")
else:
    print(f"A letra {letra} é uma vogal")