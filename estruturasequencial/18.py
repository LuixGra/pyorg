mb = float(input("Digite o tamanho do download em MB: "))
vel = float(input("Quantos megabytes por segundo: "))
 
t = (mb / vel) / 60

print(f"Vai demorar {t:.2f} minutos para se fazer o download")