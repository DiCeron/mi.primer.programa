mi_lista = []
input_usuario = input("¿Que desea agregar a su lista de compra? (Para terminar su lista escriba Fin): ")

while input_usuario != "Fin":
    mi_lista.append(input_usuario)
    input_usuario = input("¿Que desea agregar a su lista de compra? (Para terminar su lista escriba Fin): ")

for item in mi_lista:
    print("Debes comprar {}".format(item))
print("Esta es tu lista de compra")