"""
Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
- Debe detectar automáticamente de qué tipo se trata y realizarla conversión.
- En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ". (Alt+0151 —)
- El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
"""

def stringArray (texto):
    posicionInicial = 0
    palabras = []
    
    if (texto[0] == "." or texto[0] == "—"):
        
        for i in range (0, len(texto), 1):
                
            if ((texto[i] == " " and texto[i + 1] == " ") or i == (len(texto) - 1)):
                palabra = []
                
                posicionFinal = i + 1
                
                posicionInicialSimbolo = posicionInicial
                
                for j in range (posicionInicial, posicionFinal, 1):
                    
                    if (texto[j] == " " or j == (len(texto) - 1)):
                        letra = ""
                        
                        if (j == (len(texto) - 1)):
                            posicionFinalSimbolo = j + 1
                            
                        else:
                            posicionFinalSimbolo = j
                        
                        for k in range (posicionInicialSimbolo, posicionFinalSimbolo, 1):
                            letra += texto[k]
                            
                        palabra.append(letra)
                        posicionInicialSimbolo = j + 1
                    
                posicionInicial = i + 2
                palabras.append(palabra)
                
    else:
        
        for i in range (0, len(texto), 1):
                
            if (texto[i] == " " or i == (len(texto) - 1)):
                palabra = ""
                
                if (i == (len(texto) - 1)):
                    posicionFinal = i + 1
                    
                else:
                    
                    posicionFinal = i
                
                for j in range (posicionInicial, posicionFinal, 1):
                    palabra += texto[j]
                    
                posicionInicial = i + 1
                palabras.append(palabra)
    
    if (texto[0] == "." or texto[0] == "—"):
        
        print("Resultado de la Conversion:")
        conversionArregloMorse(palabras)
        
    else:
        
        print("Resultado de la Conversion:")
        conversionArregloNatural(palabras)

def conversionArregloMorse (arregloPalabras):
    
    arregloConversor = [] #0 - 38
    arregloConversor.append(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ","])
    arregloConversor.append([".—", "—...", "—.—.", "—..", ".", "..—.", "——.", "....", "..", ".———", "—.—", ".—..", "——", "—.", "——.——", "———", ".——.", "——.—", ".—.", "...", "—", "..—", "...—", ".——", "—..—", "—.——", "——..", "—————", ".————", "..———", "...——", "....—", ".....", "—....", "——...", "———..", "————.", ".—.—.—", "——..——"])
    arregloConvertido = []
    resultadoFinal = ""
        
    for i in range (0, len(arregloPalabras), 1):
        palabraConvertida = ""
        
        for j in range (0, len(arregloPalabras[i]), 1):
                
            for k in range (0, 39, 1):
                    
                if (arregloPalabras[i][j] == arregloConversor[1][k]):
                        
                    palabraConvertida += arregloConversor[0][k]
                    
        arregloConvertido.append(palabraConvertida)
        
    for i in range (0, len(arregloConvertido), 1):
        resultadoFinal += arregloConvertido[i] + " "
        
    print(resultadoFinal)

def conversionArregloNatural (arregloPalabras):
    
    arregloConversor = [] #0 - 38
    arregloConversor.append(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ","])
    arregloConversor.append([".—", "—...", "—.—.", "—..", ".", "..—.", "——.", "....", "..", ".———", "—.—", ".—..", "——", "—.", "——.——", "———", ".——.", "——.—", ".—.", "...", "—", "..—", "...—", ".——", "—..—", "—.——", "——..", "—————", ".————", "..———", "...——", "....—", ".....", "—....", "——...", "———..", "————.", ".—.—.—", "——..——"])
    arregloConvertido = []
    resultadoFinal = ""
        
    for i in range (0, len(arregloPalabras), 1):
        palabraConvertida = ""
        
        for j in range (0, len(arregloPalabras[i]), 1):
                
            for k in range (0, 39, 1):
                    
                if (arregloPalabras[i][j] == arregloConversor[0][k]):
                        
                    palabraConvertida += arregloConversor[1][k] + " "
                    
        arregloConvertido.append(palabraConvertida)
        
    for i in range (0, len(arregloConvertido), 1):
        
        resultadoFinal += arregloConvertido[i] + "/"
        
    print(resultadoFinal)

texto = input("Digite el texto que desea convertir: ")

stringArray(texto)