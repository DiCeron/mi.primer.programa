nombre = input("ingresa tu nombre: ")
grupo = input("ingresa tu grupo: ")
cuaderno = float(input("Ingresa tu calificacion de cuaderno: "))
trabajo =  float(input("ingresa tu calificacion de trabajo de investigacion: "))
participacion = float(input("ingresa tu calificacion de participacion: "))
examen= float(input("ingresa calificacion de examen: "))
tarea = float(input("ingresa calificacion de tareas: "))
cuaderno_p = cuaderno * .12
trabajo_p = trabajo * .13
parti = participacion * .20
exa = examen * .45
tare =  tarea * .10
cf = cuaderno_p + trabajo_p + parti + exa + tare
print("La calificacion de {} del grupo {} es {}".format(nombre, grupo, cf))