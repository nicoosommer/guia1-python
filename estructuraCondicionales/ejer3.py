año=int(input("Ingrese un año: "))
bisiesto=""
if año%4==0:
    if año%100==0:
        if año%400==0:
            bisiesto="es bisiesto"
        else: 
            bisiesto="no es bisiesto"
    else: 
        bisiesto="es bisiesto"
else:
    bisiesto="no es bisiesto"

print(f"El año que ingreso {bisiesto}")