frente=int(input("Ingrese la medida de frente del terreno: "))
fondo=int(input("Ingrese la medida de fondo del terreno: "))
tipo=""
superficie=0
if frente==fondo:
    tipo="cuadrado"
    superficie=frente*fondo
else:
    tipo="rectangulo"
    superficie=frente*fondo
print(f"El terreno es un {tipo} y su superficie es de {superficie}")