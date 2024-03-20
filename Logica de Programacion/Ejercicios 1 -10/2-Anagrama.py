"""
  Escribe una función que reciba dos palabras (String) y retorne
  verdadero o falso (Bool) según sean o no anagramas.
  - Un Anagrama consiste en formar una palabra reordenando TODAS
    las letras de otra palabra inicial.
  - NO hace falta comprobar que ambas palabras existan.
  - Dos palabras exactamente iguales no son anagrama.
"""
a = input("Digite la primera palabra:")
b = input("Digite la segunda palabra:")

def anagrama(a, b):
    comparador = b
    if len(a) != len(b):
        return False
    elif a == b:
        return False
    for i in a:
        contador = 0
        temporal = ""
        for j in comparador:
            if i == j:
                if contador == 0:
                    contador = contador + 1
                else:
                    temporal = temporal + j
            else:
                temporal = temporal + j
        comparador = temporal
    if comparador == "":
        return True
    else:
        return False

print(anagrama(a, b))
