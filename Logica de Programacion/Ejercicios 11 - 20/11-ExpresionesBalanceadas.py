"""
Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
- Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
- Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
- Expresión balanceada: { [ a * ( c + d ) ] - 5 }
- Expresión no balanceada: { a * ( c + d ) ] - 5 }
"""

expresion = input("Digite la expresion para validar: ")
almacenador = ["Inicial"]

for i in range (0, len(expresion), 1):
    
    if (expresion[i] == "(" or expresion[i] == "[" or expresion[i] == "{"):
        
        almacenador.append(expresion[i])
    
    elif (expresion[i] == ")"):
        
        if (almacenador[len(almacenador) - 1] == "("):
            almacenador.pop()
        else:
            almacenador.append("Error")
            break
        
    elif (expresion[i] == "]"):
        
        if (almacenador[len(almacenador) - 1] == "["):
            almacenador.pop()
        else:
            almacenador.append("Error")
            break
        
    elif (expresion[i] == "}"):
        
        if (almacenador[len(almacenador) - 1] == "{"):
            almacenador.pop()
        else:
            almacenador.append("Error")
            break

if (almacenador == [] or almacenador == ["Inicial"]):
    print("La expresion tiene los agrupadores balanceados")
else:
    print("La expresion NO tiene los agrupadores balanceados")
    