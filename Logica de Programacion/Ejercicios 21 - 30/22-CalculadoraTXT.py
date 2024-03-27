"""
Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su resultado e imprímelo.
- El .txt se corresponde con las entradas de una calculadora.
- Cada línea tendrá un número o una operación representada por un símbolo (alternando ambos).
- Soporta números enteros y decimales.
- Soporta las operaciones suma "+", resta "-", multiplicación "*" y división "/".
- El resultado se muestra al finalizar la lectura de la última línea (si el .txt es correcto).
- Si el formato del .txt no es correcto, se indicará que no se han podido resolver las operaciones.
"""

with open("Logica de Programacion/Utilidades/22-DatosCalculadora.txt", "r") as lectura:
    
    archivo = lectura.readlines()
    caracteres = []
    
    for i in range (0, len(archivo) - 1, 1):
        caracter = ""
        
        for j in range (0, len(archivo[i]) - 1, 1):
            caracter += archivo[i][j]
        
        caracteres.append(caracter)
    
    caracteres.append(archivo[-1])

consecutivo = []
pasar = 0
    
for j in range (0, len(caracteres), 1):
    resultado = 0
    
    if (pasar == 1):
        pasar = 0
        continue
    
    if (caracteres[j] == "*" or caracteres[j] == "/"):
        
        if (caracteres[j] == "*"):
            resultado = int(consecutivo.pop()) * int(caracteres[j + 1])
            consecutivo.append(resultado)
            pasar += 1
            
        elif (caracteres[j] == "/"):
            resultado = int(consecutivo.pop()) / int(caracteres[j + 1])
            consecutivo.append(resultado)
            pasar += 1
    
    else:
        consecutivo.append(caracteres[j])

pasar = 0
resultado = 0

for j in range (0, len(consecutivo), 1):
    
    if (pasar == 1):
        pasar = 0
        continue
        
    if (consecutivo[j] == "+"):
        resultado = resultado + int(consecutivo[j + 1])
        pasar += 1
        
    elif (consecutivo[j] == "-"):
        resultado = resultado - int(consecutivo[j + 1])
        pasar += 1
        
    else:
        resultado += int(consecutivo[j])
                
print(caracteres)
print(consecutivo)
print(resultado)