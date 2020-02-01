texto = input("introduce un texto: ")


mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

n_mayusculas = 0

for mayus in texto :
    if mayus in mayusculas:
        n_mayusculas += 1

print("Mayusculas= {}".format(n_mayusculas))