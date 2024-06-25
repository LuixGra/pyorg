peso = float(input("Digite o peso da pesca de hoje: "))

excesso = 0

if peso >= 50:
    excesso = peso - 50;

multa = excesso * 4.00

print(f"O peso da pesca foi de {peso}KG, o excesso foi de {excesso}KG e a multa será de {multa} reais")