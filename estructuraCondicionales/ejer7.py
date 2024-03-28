import random
dado=[1,2,3,4,5,6]
tirada=random.choice(dado)
apuesta=int(input("Ingrese lo que crea que va a salir en el dado, del 1 al 6: "))
if apuesta==tirada:
    print(f"Su apuesta fue correcta! Salio el {tirada}")
else:
    print(f"Su apuesta fue incorrecta. Salio el {tirada}")
