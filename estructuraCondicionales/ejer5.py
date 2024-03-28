import random
moneda=["cara", "cruz"]
apuesta=input("Ingrese lo que crea que va a salir, cara o cruz: ")
tirada=random.choice(moneda)
if apuesta.lower()==tirada:
    print(f"Su apuesta fue correcta! Salio {tirada}")
else:
    print(f"Su apuesta fue incorrecta. Salio {tirada}")
