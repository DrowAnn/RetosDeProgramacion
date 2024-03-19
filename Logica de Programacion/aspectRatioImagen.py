"""
Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
- Url de ejemplo: https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
- Url Funcional: https://www.imprentaonline.net/blog/wp-content/uploads/DALL%C2%B7E-2023-10-16-10.41.49-Illustration-depicting-a-humanoid-robot-with-half-of-its-face-transparent-revealing-intricate-circuits-and-gears-inside.-The-robot-is-holding-a-light-1.png
- Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.
"""

from PIL import Image

def aspectRatio (tamaño):
    if (tamaño[0]<tamaño[1]): menor = tamaño[0]
    else: menor = tamaño[1]

    for i in range (1, (menor + 1), 1):
        if ((tamaño[0] % i == 0) and (tamaño[1] % i == 0)):
            simplificados = [int(tamaño[0] / i), int(tamaño[1] / i)]

    return simplificados

imagen = Image.open("./Logica de Programacion/Utilidades/20231024_Logo Orva Blanco Fondo Azul.png")

print("Tamaño original: {}".format(imagen.size))

aspectRatio = aspectRatio(imagen.size)

print("La relación de aspecto de la imagen es {}:{}".format(aspectRatio[0],aspectRatio[1]))

