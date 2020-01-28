number_to_guess = 5
print("adivina el numero")
user_number = int(input("ingresa el numero:\n "))
if number_to_guess == user_number:
    print("has ganado")
else:
    print("has perdido")
    user_number = int(input("intentalo de nuevo:\n "))
    if number_to_guess == user_number:
        print("has ganado")
    else:
        print("has perdido")
        user_number = int(input("intentalo de nuevo:\n "))
        if number_to_guess == user_number:
            print("has ganado")
        else:
            print("has perdido")
            user_number = int(input("intentalo de nuevo:\n "))
            if number_to_guess == user_number:
                print("has ganado")
            else:
                print("has perdido")
                user_number = int(input("intentalo de nuevo:\n "))
                if number_to_guess == user_number:
                    print("has ganado")
                else:
                    print("no te quedan mas intentos, has perdido")
