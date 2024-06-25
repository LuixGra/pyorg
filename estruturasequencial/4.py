notas = []
for i in range(4):
    notas.append(float(input("Digite uma nota: ")))
    
s = 0

for nota in notas:
    i = 0
    
    s += notas[i]

    i += 1

m = s / len(notas)

print(f"A media foi de {m}")

