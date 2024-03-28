meses={1:"Enero",2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",6:"Junio",7:"Julio",8:"Agosto",9:"Septiembre",10:"Octubre",11:"Noviembre",12:"Diciembre"}
num=int(input("Ingrese el numero de mes: "))
if num in meses:
    print(f"El mes {num} es {meses[num]}")
else:
    print("Numero invalido")