"""
Escribe un programa que se encargue de comprobar si un número es o no primo. Hecho esto, imprime los números primos entre 1 y 100.
"""

num = int(input("Digite un numero: "))
contador = 0

for i in range(1,(num + 1), 1):
    if (num % i == 0):
        contador += 1

if (contador == 2): print("{} es primo".format(num))
else: print("{} no es primo".format(num))

print("Lista de numero primos entre 1 y 100")

for i in range (2, 101, 1):
    contador = 0
    for j in range(1,(i + 1), 1):
        if (i % j == 0):
            contador += 1
    if (contador == 2): print(str(i))