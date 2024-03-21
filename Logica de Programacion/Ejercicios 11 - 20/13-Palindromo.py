"""
Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.
- Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
- NO se tienen en cuenta los espacios, signos de puntuación y tildes.
- Ejemplo: ana lleva al oso, la avellana.
"""

palabra = input("Digite la palabra para verificar: ")
palabraSimplificada = ""
palabraReves = ""

for i in range (0, len(palabra), 1):
    
    if (palabra[i] == " " or palabra[i] == "." or palabra[i] == ","):
        pass
    else:
        palabraSimplificada = palabraSimplificada + palabra[i]
        palabraReves = palabra[i] + palabraReves

print(palabraSimplificada == palabraReves)
    