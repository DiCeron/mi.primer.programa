texto = input("introduce un texto: ")

comas = [","]
puntos = ["."]
espacios = [" "]

n_comas = 0
n_puntos = 0
n_espacios = 0

for signos in texto:
    if signos in comas:
        n_comas += 1
    elif signos in puntos:
        n_puntos += 1
    elif signos in espacios:
        n_espacios += 1

print("Comas = {}".format(n_comas))
print("Puntos = {}".format(n_puntos))
print("Espacios = {}".format(n_espacios))