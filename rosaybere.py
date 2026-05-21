#nombre de los integrantes: berenice guadalupe cahuich maldonado y rosa elena utuy santos
#nombre del trabajo: tienda de descuentos
#nombre del docente: wilfrido david castillo lugo
#fecha de elaboracion: 18/05/26

total = float(input("ingresa el total de compra: "))
color = input("ingresa el color de la bolita: ")

if color == "rojo":
    descuento = total * 0.40
    pagar = total - descuento 

elif color == "amarillo":
    descuento = total * 0.25 
    pagar = total - descuento 

else: 
    pagar = total

print("el cliente pagara: ", pagar)