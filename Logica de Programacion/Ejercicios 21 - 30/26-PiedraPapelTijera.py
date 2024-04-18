"""
Crea un programa que calcule quien gana más partidas al piedra, papel, tijera.
- El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
- La función recibe un listado que contiene pares, representando cada jugada.
- El par puede contener combinaciones de "R" (piedra), "P" (papel) o "S" (tijera).
- Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
"""
arreglo = [("R","S"), ("S","R"), ("P","S"), ("S", "P")]
jugador1 = 0
jugador2 = 0

for dupla in arreglo:
    if (dupla[0] == "R" and dupla[1] == "S"):
        jugador1 += 1
    elif (dupla[0] == "R" and dupla[1] == "P"):
        jugador2 += 1
    elif (dupla[0] == "S" and dupla[1] == "R"):
        jugador2 += 1
    elif (dupla[0] == "S" and dupla[1] == "P"):
        jugador1 += 1
    elif (dupla[0] == "P" and dupla[1] == "R"):
        jugador1 += 1
    elif (dupla[0] == "P" and dupla[1] == "S"):
        jugador2 += 1

if (jugador1 == jugador2):
    print("Tie")
elif (jugador1 > jugador2):
    print("Jugador 1")
else:
    print("Jugador 2")