import sys

consumo = float(input("quanto foi o KWH?"))
qualTuaBandeira = input("bandeira é: VERD, AMA ou VERM").upper()

acrescimo = 0
valor = 0

if qualTuaBandeira == "VERD":
    acrescimo = 1
elif qualTuaBandeira == "AMA":
    acrescimo = 1.1
elif qualTuaBandeira == "VERM":
    acrescimo = 1.2
else:
    print("sua bandeira não existe")
    sys.exit(1)

valorConsumo = 0

if consumo <= 100:
    valorConsumo = consumo * 0.5
elif consumo >= 101 and consumo <= 200:
    valorConsumo = consumo * 0.7
else:
    valorConsumo = consumo * 0.87

valorSemBandeira = valorConsumo + 15
valorAcrescimoBandeira =  valorSemBandeira * acrescimo

print("valorConsumo", valorConsumo, "acrescimo", (valorAcrescimoBandeira) - valorSemBandeira, "iluminação taxa", 15, "final", valorAcrescimoBandeira)
