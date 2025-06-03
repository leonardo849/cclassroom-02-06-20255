import classes
import sys


def ePositivo(num):
    if num >= 0:
        return True
    else:
        return False

def estaEntre(min, max, num):
    if num >= min and num <= max:
        return True
    else:
        return False
    

def ePar(num):
    return num % 2 == 0

def saqueEValido(min, max, num):
    return ePositivo(num) and estaEntre(min, max, num) and ePar(num)

def  divideEPreparaOValor(value, dividirPor):
    valor = str(value/dividirPor)
    resultadoDivisao = valor[0:valor.index(".")]
    return int(resultadoDivisao)


    

def retorneCedulas(value):
    valorDescontado = value
    notas = []


    print(notas, valorDescontado)

    while valorDescontado >= 2:
        if (valorDescontado % 10 == 6 or valorDescontado % 10 == 8) and valorDescontado <= 8:
            quantidade = divideEPreparaOValor(valorDescontado, 2)
            nota = classes.Nota(2, quantidade)
            notas.append(nota)
            valorDescontado -= quantidade * 2
        elif valorDescontado >= 2 and valorDescontado < 5:
            quantidade = divideEPreparaOValor(valorDescontado, 2)
            nota = classes.Nota(2, quantidade)
            notas.append(nota)
            valorDescontado -= quantidade * 2
        elif valorDescontado >= 5 and valorDescontado < 10:
            quantidade = divideEPreparaOValor(valorDescontado, 5)
            nota = classes.Nota(5, quantidade)
            notas.append(nota)
            valorDescontado -= quantidade * 5

        elif valorDescontado >= 10 and valorDescontado < 20:
            quantidade = divideEPreparaOValor(valorDescontado, 10)
            nota = classes.Nota(10, quantidade)
            notas.append(nota)
            valorDescontado -= quantidade * 10
        elif valorDescontado >= 20 and valorDescontado < 50:
            quantidade = divideEPreparaOValor(valorDescontado, 20)
            nota = classes.Nota(20, quantidade)
            notas.append(nota)
            valorDescontado -= quantidade * 20
        elif valorDescontado >= 50 and valorDescontado < 100:
            quantidade = divideEPreparaOValor(valorDescontado, 50)
            print(quantidade)
            nota = classes.Nota(50, quantidade)
            notas.append(nota)
            valorDescontado -= quantidade * 50
        else:
            quantidade = divideEPreparaOValor(valorDescontado, 100)
            print(quantidade)
            nota = classes.Nota(100, quantidade)
            notas.append(nota)
            valorDescontado -= quantidade * 100

        
            


    
    print(valorDescontado)


    print("Notas:", notas)
    return notas
