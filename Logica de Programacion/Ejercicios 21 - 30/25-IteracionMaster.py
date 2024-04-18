"""
Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
¿De cuántas maneras eres capaz de hacerlo?
Crea el código para cada una de ellas.
"""
#Metodo 1
n = 1
while (n < 101):
    print(n)
    n += 1

#Metodo 2
for i in range (1, 101, 1):
    print(i)

#Metodo 3
def contarHasta100Desde (n):
    if (n <= 100):
        print(n)
        contarHasta100Desde(n + 1)
        
contarHasta100Desde(1)