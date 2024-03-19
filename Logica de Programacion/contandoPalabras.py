"""
Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
- Los signos de puntuación no forman parte de la palabra.
- Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
- No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
"""

texto = input("Digite el texto que desea analizar: ")
posicionInicial = 0
posicionFinal = 0
palabras = []
arregloPalabras = []
arregloContador = []
signosPuntuacion = [".", ",", ";", ":", "{", "}", "(", ")", "[", "]", "'", '"', "¿", "?", "¡", "!", "..."]

for i in range (0, len(texto), 1):

    if ((texto[i] == " ") or (i == (len(texto) - 1))):

        if (i == (len(texto) - 1)): posicionFinal = i + 1
        else: posicionFinal = i

        palabra = ""

        for j in range (posicionInicial, posicionFinal, 1):
            contadorPuntuacion = 0

            for k in range (0, len(signosPuntuacion), 1):
                
                if (texto[j] == signosPuntuacion[k]):
                    contadorPuntuacion += 1
            
            if (contadorPuntuacion == 0):
                palabra = palabra + texto[j]

        palabras.append(palabra)
        posicionInicial = i + 1

arregloPalabras.append(palabras[0])
arregloContador.append(0)

for i in range (0, len(palabras), 1):
    existencia = 0

    for j in range (0, len(arregloPalabras), 1):

        if (palabras[i] == arregloPalabras[j]):
            arregloContador[j] += 1
        else:
            existencia += 1

        if (existencia == len(arregloPalabras)):
            arregloPalabras.append(palabras[i])
            arregloContador.append(1)

for i in range (0, len(arregloContador), 1):
    print("{}. {} = {}".format((i + 1), arregloPalabras[i], arregloContador[i]))