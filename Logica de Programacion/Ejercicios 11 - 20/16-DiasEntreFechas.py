"""
Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
- Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
- La función recibirá dos String y retornará un Int.
- La diferencia en días será absoluta (no importa el orden de las fechas).
- Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.
"""

def capturaFecha (fecha):
    
    if (len(fecha) == 10):
        contador = 0
        numero = ""
        arregloFecha = []
        
        for i in range (0, len(fecha), 1):
            
            for j in range (0, 10, 1):
                
                try:
                    
                    if (fecha[i] == "/"):
                        pass
                    elif (int(fecha[i]) == j):
                        pass
                    
                except:
                    print('Error de digitacion, la fecha solo debe contener numero y los separadores "/"')
                    return capturaFecha (input("Digite una nueva fecha en formato dd/mm/yyyy: "))
            
            if (fecha[i] == "/"):
                contador += 1
                
                if (contador == 1):
                    
                    if (len(numero) == 2 and int(numero) > 0 and int(numero)<= 31):
                        arregloFecha.append(numero)
                        numero = ""
                    else:
                        print("Error de digitacion, el dia de la fecha debe estar entre 00 y 31, con dos digitos")
                        return capturaFecha (input("Digite una nueva fecha en formato dd/mm/yyyy: "))
                    
                elif (contador == 2):
                    
                    if (len(numero) == 2 and int(numero) > 0 and int(numero)<= 12):
                        arregloFecha.append(numero)
                        numero = ""
                    else:
                        print("Error de digitacion, el mes de la fecha debe estar entre 00 y 12, con dos digitos")
                        return capturaFecha (input("Digite una nueva fecha en formato dd/mm/yyyy: ")) 
            
            else: 
                numero += fecha[i]
        
        arregloFecha.append(numero)
        return arregloFecha
      
    else:
        print("La fecha es incorrecta, revise que el formato ingresado sea dd/mm/yyyy: ")
        return capturaFecha (input("Digite una nueva fecha en formato dd/mm/yyyy: "))
    
fecha1 = capturaFecha(input("Digite la primera fecha en formato dd/mm/yyyy: "))
print("")
fecha2 = capturaFecha(input("Digite la segunda fecha en formato dd/mm/yyyy: "))
    
dias = (int(fecha1[0]) - int(fecha2[0])) + ((int(fecha1[1]) - int(fecha2[1])) * 30) + ((int(fecha1[2]) - int(fecha2[2])) * 360)
    
print(f"La diferencia entre las fechas es de {abs(dias)} dias")