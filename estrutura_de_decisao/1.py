#Faça um Programa que peça dois números e imprima o maior deles.

n = []
for i in range(0,2):
    n.append(float(input("Digite um nmr: ")))
maior = max(n)

print(f"O maior numero foi {maior}")