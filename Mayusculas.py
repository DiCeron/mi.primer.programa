texto = input("introduce un texto: ")

mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
mayus = []
n_mayusculas = 0

for mayu in texto:
    if mayu in mayusculas:
        n_mayusculas += 1
        mayus.append(mayu)

print("Mayusculas= {}".format(n_mayusculas))
print(mayus)