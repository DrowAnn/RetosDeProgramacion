"""
Crea una función que evalúe si un/a atleta ha superado correctamente una carrera de obstáculos.
- La función recibirá dos parámetros:
  - Un array que sólo puede contener String con las palabras "run" o "jump"
  - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
- La función imprimirá cómo ha finalizado la carrera:
  - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no variará el símbolo de esa parte de la pista.
  - Si hace "jump" en "_" (suelo), se variará la pista por "x".
  - Si hace "run" en "|" (valla), se variará la pista por "/".
- La función retornará un Boolean que indique si ha superado la carrera.
Para ello tiene que realizar la opción correcta en cada tramo de la pista.
"""

atleta = ["run", "jump", "run", "jump", "run", "ran", "run", "run", "run", "jump", "run"]
pista = "_|_|_____|_"

def carreraObstaculos (pista, atleta):
    contador = 0
    finalCarrera = ""
    
    if (len(atleta) < len(pista)):
        return "El atleta no termino la carrera"
    
    for i in range (0, len(pista)):
        
        if (atleta[i] != "run" and atleta[i] != "jump"):
            return f"El atleta hizo un movimiento no permitido en la accion numero {i + 1}"
        
        if ((atleta[i] == "run" and pista[i] == "_") or (atleta[i] == "jump" and pista[i] == "|")):
            
            contador += 1
            finalCarrera += pista[i]
            
        elif (atleta[i] == "run" and pista[i] == "|"):
            
            finalCarrera += "/"
    
    print(finalCarrera)
    return contador == len(pista)

print(carreraObstaculos(pista, atleta))