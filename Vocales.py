texto_usuario = input("Ingrese un texto: ")

vocales_naturales = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]

vocales_del_texto = []

n_vocales = 0

for vocal in texto_usuario:
    if vocal in vocales_naturales:
        n_vocales += 1
        vocales_del_texto.append(vocal)
print(vocales_del_texto)