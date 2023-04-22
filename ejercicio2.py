# ejercicio 2_Mostrar e inprimir cuantos multiplos de 7 y cuantos multiplos de 9 hay entre mil y 5000
#Se declaran tres variables para definir el rango y almacenar los multiplos de 7 y 9
x=range(1000,5000)
mult_7=0
mult_9=0

#Processing
for i in x:
    if i%7==0 and i%9==0:
        mult_7+=1
        mult_9+=1
    elif i%7==0:
        mult_7+=1
    elif i%9==0:
        mult_9+=1

#Output
print(f"En el rango (1000,5000) hay {mult_7} multiplos de 7")
print(f"En el rango (1000,5000) hay {mult_9} multiplos de 9")