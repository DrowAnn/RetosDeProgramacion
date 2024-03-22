"""
Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.
"""

def factorialNumero (numero):
    
    if (numero < 0): 
        return None
    elif (numero <= 1):
        return 1
    else:
        return numero * factorialNumero(numero-1)

numero = int(input("Digite un numero para calcular el Factorial: "))

print(factorialNumero(numero))