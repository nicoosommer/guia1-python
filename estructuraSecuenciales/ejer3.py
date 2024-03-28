segundos=int(input("Ingrese la cantidad de segundos: "))
dia=86400
hora=3600
minuto=60

dias=segundos//dia
segundos=segundos-dia*dias
horas=segundos//hora
segundos=segundos-horas*hora
minutos=segundos//minuto
segundos=segundos-minutos*minuto
print(f"Hay {dias} dias, {horas} horas, {minutos} minutos y {segundos} segundos")