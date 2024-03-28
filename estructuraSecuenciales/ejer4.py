lado1=int(input("Ingrese el lado1: "))
lado2=int(input("Ingrese el lado2: "))
lado3=int(input("Ingrese el lado3: "))
perimetro=lado1+lado2+lado3
s=(lado1+lado2+lado3)/2
area=(s*(s-lado1)*(s-lado2)*(s-lado3))**.5
print(f"EL perimetro es {perimetro} y el area es {area}")