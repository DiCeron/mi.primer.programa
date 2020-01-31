number_to_guess = 5
print("adivina el numero del 1 al 5")
user_number = int(input("ingresa el numero: "))
while number_to_guess> 0 and user_number <5:
    if number_to_guess == user_number:
        print("has ganado")
    else:
        user_number = int(input("intentalo de nuevo: "))
print("Has ganado")