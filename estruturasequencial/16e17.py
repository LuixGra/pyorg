import math

area = float(input("Digite a área a ser pintada: "))

lata_litro = 18
galao_litro = 3.6

lata_preco = 80
galao_preco = 25

preco_total = float()

latas_necessarias = 0
galoes_necessarios = 0
litros_tinta = area / 6


def calculaLata(area):
    latas_necessarias = math.ceil(litros_tinta/lata_litro) 
    preco_total = latas_necessarias * lata_preco
    return preco_total, latas_necessarias

preco_total, latas_necessarias= calculaLata(area)
print(f"Sera necessário {litros_tinta} litros de tinta, custando R${preco_total:.2f} se comprar apenas latas de tinta, utilizando {latas_necessarias} latas")


def calculaGalao(area):
    galoes_necessarios = math.ceil(litros_tinta/galao_litro)
    preco_total = galoes_necessarios * galao_preco
    return preco_total, galoes_necessarios

preco_total, galoes_necessarios = calculaGalao(area)

print(f"Da mesma forma, seriam necessarios {galoes_necessarios} galoes para pintar {area} M², custando R${preco_total:.2f}")

#combinando galoes e latas

def calculaMistura(area):
    latas_mistas = int(litros_tinta//lata_litro)
    litros_restantes = litros_tinta % lata_litro
    galoes_mistos = math.ceil(litros_restantes / galao_litro)
    preco_total = (latas_mistas * lata_preco) + (galoes_mistos * galao_preco)

    return latas_mistas, galoes_mistos, preco_total

latas_mistas, galoes_mistos, preco_total = calculaMistura(area)

print(f"E utilizando galoes e latas, serão necessários {galoes_mistos} galões e {latas_mistas} latas, custando R${preco_total:.2f}")