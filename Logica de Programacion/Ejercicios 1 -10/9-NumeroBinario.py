"""
* Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones
propias del lenguaje que lo hagan directamente.
"""

numeroDecimal = int(input("Digite el numero que desea convertir a Binario: "))

def conversionBinario (numeroDecimal):
    numeroBinario = ""
    
    for i in range (200, -1, -1):
        
        if ((2 ** i) <= numeroDecimal):
            
            for j in range (i, -1, -1):
                if (numeroDecimal - (2 ** j) >= 0):
                    numeroBinario += "1"
                    numeroDecimal -= (2 ** j)
                else:
                    numeroBinario += "0"
                    
            break
    
    return numeroBinario
            
print(f"El numero decimal {numeroDecimal} convertido a Binario es: {conversionBinario(numeroDecimal)}")