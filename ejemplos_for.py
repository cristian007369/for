# ejemplo 1
rta="salida = |"
for i in [1,2,3,4,5,6,7,8,9,10]:
    rta= rta + str( i )+ ", "
rta=rta+ " |"
print(rta)

# ejemplo 2
for i in [1,2,3,4,5,6,7,8,9,10]:
    print("UIS no es uno...")

# ejemplo 3
rta="salida = |"
for i in (1,2,3,4,5,6,7,8,9,10):
    rta= rta + str( i )+ ", "
rta=rta+ " |"
print(rta)

# ejemplo 4
rta="salida = |"
for i in range(1,11):
    rta= rta + str( i )+ ", "
rta=rta+ " |"
print(rta)

# ejemplo 5
rta="salida = |"
for i in "UIS no es uno":
    rta= rta + str( i )+ ", "
rta=rta+ " |"
print(rta)

# ejemplo 6
suma=0
for i in range(1,11):
    suma += i
print(f"La suma es: {suma}")

# ejemplo 7
frase=input("Digite una frase: ") 
vocales="aeiouAEIOU"
numero_vocales=0
for i in frase:
    if i in vocales:
        numero_vocales+=1
print(f"En la frase hay {numero_vocales} vocales")