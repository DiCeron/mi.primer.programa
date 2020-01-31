operacion = input("¿Qué operación desea realizar? ( sumar, restar, dividir, multiplicar):")

primer_numero = float(input("Introduce el primer numero: "))

segundo_numero = float(input("introduce el segundo numero: "))

if operacion == "sumar":
    suma = primer_numero + segundo_numero
    print("El resultado de la suma entre {} y {} es {}".format(primer_numero, segundo_numero, suma))

elif operacion == "restar":
    resta = primer_numero - segundo_numero
    print("El resultado de la resta entre {} y {} es {}".format(primer_numero, segundo_numero, resta))

elif operacion == "dividir":
    division = primer_numero / segundo_numero
    print("El resultado entre la divisón entre {} y {} es {}".format(primer_numero, segundo_numero, division))

elif operacion == "miltiplicar":
    multi = primer_numero * segundo_numero
    print("El resultado de la multiplicación de {} por {} es {}".format(primer_numero, segundo_numero, multi))