"""
Crea una función que reciba un String de cualquier tipo y se encargue de poner en mayúscula la primera letra de cada palabra.
- No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
"""

texto = input("Digite un texto: ")
textoMayusculas = []
i = 0

while i < len(texto):
    
    if (i == 0):
        textoMayusculas.append(texto[i].upper())
        i += 1
        continue
        
    if (texto[i] == " "):
        textoMayusculas.append(" " + texto[(i + 1)].upper())
        i += 2
    else:
        textoMayusculas.append(texto[i])
        i += 1
          
print("".join(textoMayusculas))