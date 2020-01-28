helado_q = input("¿quieres un helado? ( si / no ): ")
money_q = input("¿tienes dinero para un helado? ( si / no ): ")
sr_q = input("¿esta el señor de los helados? ( si / no ): ")
family_q = input("¿esta un familiar contigo? ( si / no ): ")

helado = helado_q == "si"
money = money_q == "si" or family_q == "si"
sr = sr_q == "si"

if helado  and money and sr :
    print("compra un helado")
else:
    print("no puedes comprar un helado")