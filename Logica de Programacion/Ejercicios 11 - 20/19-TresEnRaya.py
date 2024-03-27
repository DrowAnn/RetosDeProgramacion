"""
Crea una función que analice una matriz 3x3 compuesta por "X" y "O" y retorne lo siguiente:
- "X" si han ganado las "X"
- "O" si han ganado los "O"
- "Empate" si ha habido un empate
- "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta. O si han ganado los 2.
Nota: La matriz puede no estar totalmente cubierta. Se podría representar con un vacío "", por ejemplo.
"""

matriz = [["O", "", "X"],
          ["O", "O", "X"],
          ["O", "X", ""]]

def analisisTriqui (matriz):
    variables = ["X", "O"]
    resultado = []
    x = 0
    o = 0
    
    if (len(matriz) != 3):
        return "Nulo"
    
    for i in range (0, 3, 1):
        
        if (len(matriz[i]) != 3):
            return "Nulo"
        
        for j in range (0, 3, 1):
            
            if (matriz[i][j] == "X"):
                x += 1
            elif (matriz[i][j] == "O"):
                o += 1
                
    if (abs(x - o) > 1):
        return "Nuloe"
    
    for variable in variables:
        victorias = 0
        
        if (matriz[1][1] == variable):
                
                if(matriz[0][0] == variable and matriz[2][2] == variable):
                    victorias += 1
                    
                if(matriz[2][0] == variable and matriz[0][2] == variable):
                    victorias += 1
        
        for i in range (0, 3, 1):
            
            if (matriz[i][0] == variable and matriz[i][1] == variable and matriz[i][2] == variable):
                victorias += 1
            
            if (matriz[0][i] == variable and matriz[1][i] == variable and matriz[2][i] == variable):
                victorias += 1
        
        resultado.append(victorias)
    
    if (resultado[0] != 0 and resultado[1] != 0):
        return "Nulo"
    elif (resultado[0] == resultado[1]):
        return f"Empate {resultado}"
    elif (resultado[0] > resultado[1]):
        return "X"
    else:
        return "O"
                
print(analisisTriqui(matriz))
        