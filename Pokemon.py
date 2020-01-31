pokemon_elegido = input("Contraque pokemon quieres combatir? (Squirtle / Charmander / Bulbasaur):  ")

vida_pikachu = 100
vida_enemigo = 0
ataque_enemigo = 0

if pokemon_elegido == "Squirtle":
    vida_enemigo = 90
    ataque_enemigo = 9
    nombre_pokemon = "Squirtle"

elif pokemon_elegido == "Charmander":
    vida_enemigo = 80
    ataque_enemigo = 10
    nombre_pokemon = "Charmander"

elif pokemon_elegido == "Bulbasaur":
    vida_enemigo = 100
    ataque_enemigo = 11
    nombre_pokemon = "Bulbasaur"

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque = input("Que ataque quieres utilizar ? (Voltios /Chizpazo)")

    if ataque == "Volteos":
        vida_enemigo -= 20
        print("La vida de {} ahora es {}".format(nombre_pokemon, vida_enemigo))

    elif ataque == "Chizpazo":
        vida_enemigo -= 10
        print("La vida de {} ahora es {}".format(nombre_pokemon, vida_enemigo))

    vida_pikachu -= ataque_enemigo

    print("{} te a hecho un ataque de {} de daño".format(nombre_pokemon, ataque_enemigo))

    print("Tu vida ahora es {}".format(vida_pikachu))

    if vida_enemigo <= 0:
        print("¡Has ganado!")

    elif vida_pikachu <= 0:
        print("¡Has perdido!")

print("el combate a terminado")
