"""
Escribe una función que calcule si un número dado es un número de Armstrong (o también llamado narcisista).
"""

numero = input("Digite el numero que desea comprobar: ")
comprobador = 0

for i in range (0, len(numero), 1):
    
    comprobador += (int(numero[i]) ** len(numero))
    
print(int(numero) == comprobador)