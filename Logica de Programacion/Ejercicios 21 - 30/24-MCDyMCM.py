"""
Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra que calcule el mínimo
común múltiplo (mcm) de dos números enteros.
- No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
"""
def mcd (num1, num2):
    if (num1 > num2):
        d = num1
    else:
        d = num2
    while (d > 0):
        if (num1 % d == 0 and num2 % d == 0):
            return d
        d -= 1

def mcm (num1, num2):
    arreglonum1 = []
    arreglonum2 = []
    
    if (num1 > num2):
        d = num1 + 1
    else:
        d = num2 + 1
        
    for i in range (1, d, 1):
        arreglonum1.append(num1 * i)
        arreglonum2.append(num2 * i)

    for i in range (0, len(arreglonum1), 1):
        for j in range (0, len(arreglonum2), 1):
            if (arreglonum1[i] == arreglonum2[j]):
                return arreglonum1[i]
            
num1 = 4
num2 = 8
print(mcd(num1, num2))
print(mcm(num1, num2))