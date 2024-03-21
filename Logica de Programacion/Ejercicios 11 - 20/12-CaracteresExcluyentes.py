"""
Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
- out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
- out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.
"""

def caracteresExcluyentes (arreglo1, arreglo2):
    
    out = ""

    for i in range (0, len(arreglo1), 1):
        contador = 0
        
        for j in range (0, len(arreglo2), 1):
            
            if (arreglo1[i] == arreglo2[j]):
                contador += 1
                break
        
        if (contador == 0):
            out += arreglo1[i]

    print(out)
    
str1 = input("Digite la primera cadena: ")
str2 = input("Digite la segunda cadena: ")

caracteresExcluyentes(str1, str2)
caracteresExcluyentes(str2, str1)