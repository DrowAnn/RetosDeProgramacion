"""
Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

cadenaOriginal = input("Digite la cadena a Invertir: ")
cadenaInvertida = ""

for i in range (0, len(cadenaOriginal), 1):
    cadenaInvertida = cadenaOriginal[i] + cadenaInvertida

print("La cadena Invertida es: {}".format(cadenaInvertida))