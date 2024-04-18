def conjuntos(arreglo1, arreglo2, booleano):
    resultado1 = []
    resultado2 = []
    
    for i in range (0, len(arreglo1), 1):
        for j in range (0, len(arreglo2), 1):
            if (arreglo1[i] == arreglo2[j]):
                resultado1.append(arreglo1[i])
                break
    
    arreglo3 = arreglo1 + arreglo2
    
    for i in range (0, len(arreglo3), 1):
        c = 0
        for j in range (0, len(resultado1), 1):
            if (arreglo3[i] != resultado1[j]):
                c += 1
            else:
                break
        if (c == len(resultado1)):
            resultado2.append(arreglo3[i])
            
    if (booleano):
        return resultado1
    else:
        return resultado2

arreglo1 = [1, 1, 2, 3, 4, 5, 6]
arreglo2 = [4, 5, 6, 7, 8, 9, 9]
booleano = False

print(conjuntos(arreglo1, arreglo2, booleano))