import random

# Le agrego cantidad todal de rondas
rondas_totales = 5
opciones = ["piedra", "papel", "tijera"]

print("¡Bienvenido! Vamos a jugar a Piedra, Papel o Tijera.")
print(f"El juego es al mejor de {rondas_totales} rondas.")
print("Escribí tu jugada (piedra/papel/tijera).")

ronda = 1
puntos_usuario = 0
puntos_pc = 0

while ronda <= rondas_totales:
    print(f"\nRonda {ronda}")

    # Valido la entrada para pedir jugada de nuevo
    while True:
        jugada_usuario = input("Tu jugada (piedra/papel/tijera): ").strip().lower()
        if jugada_usuario in opciones:
            break
        else:
            print("Entrada no valida. Intenta nuevamente.")

    jugada_pc = random.choice(opciones)
    print(f"La computadora eligio: {jugada_pc}")

    if jugada_usuario == jugada_pc:
        print("Empate.")
    elif (
        (jugada_usuario == "piedra" and jugada_pc == "tijera") or
        (jugada_usuario == "papel" and jugada_pc == "piedra") or
        (jugada_usuario == "tijera" and jugada_pc == "papel")
    ):
        print("¡Ganaste la ronda!")
        puntos_usuario += 1
    else:
        print("Perdiste la ronda.")
        puntos_pc += 1

    # Me fijo si el juego ya termino o no
    rondas_restantes = rondas_totales - ronda
    if puntos_usuario > puntos_pc + rondas_restantes:
        break
    if puntos_pc > puntos_usuario + rondas_restantes:
        break

    ronda += 1

print("\n=== Resultado final ===")
print(f"Tus puntos: {puntos_usuario} | Puntos de la PC: {puntos_pc}")

if puntos_usuario > puntos_pc:
    print("¡Ganaste el juego! 🎉")
elif puntos_usuario < puntos_pc:
    print("La computadora gano el juego.")
else:
    print("Empate total.")
