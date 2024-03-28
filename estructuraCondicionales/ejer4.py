palabra=input("Ingrese una palabra: ")
letras=len(palabra)
lf=palabra[letras-1].lower()
if lf=="a" or lf=="e" or lf=="i" or lf=="o"or lf=="u":
    print(f"La palabra tiene {letras} letras y su ultima letra es una vocal")
else:
    print(f"La palabra tiene {letras} letras y su ultima letra no es una vocal")