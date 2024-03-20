"""
Crea una única función (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 - La función recibirá por parámetro sólo UN polígono a la vez.
 - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 - Imprime el cálculo del área de un polígono de cada tipo.
 """

def areaPoligono (opcion):
    if (opcion == 1):
        base = int(input("Digite la base del Triangulo: "))
        altura = int(input("Digite la altura del Triangulo: "))
        return "El area del Triangulo es: {}".format((base*altura)/2)
    elif (opcion == 2):
        lado = int(input("Digite uno de los lados del Cuadrado: "))
        return "El area del Cuadrado es: {}".format(lado**2)
    elif (opcion == 3):
        base = int(input("Digite la base del Rectangulo: "))
        altura = int(input("Digite la altura del Rectangulo: "))
        return "El area del Rectangulo es: {}".format(base*altura)
    else:
        return "La opcion no esta entre las posibles"

print("Digite el numero de la opcion que le corresponda")
print("1. Triangulo")
print("2. Cuadrado")
print("3. Rectangulo")
opcion = int(input("Digite solo el numero de la opcion: "))

print(areaPoligono(opcion))