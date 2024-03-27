"""
Crea una función que reciba días, horas, minutos y segundos (como enteros) y retorne su resultado en milisegundos.
"""

def conversorMilisegundos ():
    
    datos = ["dias", "horas", "minutos", "segundos"]

    for i in range (0, 4, 1):
        datos[i] = int(input(f"Digite la cantidad de horas {datos[i]}: "))
    
    milisegundos = (((((((datos[0] * 24) + datos[1]) * 60) + datos[2]) * 60 ) + datos[3]) / 1000)

    return milisegundos

print(conversorMilisegundos())