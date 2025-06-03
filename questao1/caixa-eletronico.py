import funcoes
import sys
import variaveis


valorDoSaque = int(input("quanto vc   quer sacar?"))

podeTerSaque = funcoes.saqueEValido(variaveis.minimo, variaveis.maximo, valorDoSaque)

if podeTerSaque == False:
    print("vc n ta podendo fazer saque fi")
    sys.exit(1)

funcoes.retorneCedulas(valorDoSaque)


    

