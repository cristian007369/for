# ejercicio 1
n=int(input("Dígite un número: "))
num_pares=0
num_impares=0
for i in range(1,n+1):
    if i%2==0:
        num_pares+=1
    else:
        num_impares+=1
print(f"Hay {num_pares} números pares en {n}")
print(f"Hay {num_impares} números impares en {n}")

# ejercicio 2
x=range(1000,5000)
mult_7=0
mult_9=0
for i in x:
    if i%7==0:
        mult_7+=1
    elif i%9==0:
        mult_9+=1
print(f"En rango (1000,5000) hay {mult_7} multiplos de 7")
print(f"En rango (1000,5000) hay {mult_9} multiplos de 9")

# ejercicio 3
import random
cara1 , cara2 ,cara3 ,cara4 ,cara5 ,cara6=0 ,0 ,0 ,0 ,0 ,0 
lanzamiento=int(input("Dígite cuantas veces se va a lanzar el dado: "))
for i in range(lanzamiento):
    dado=random.randint(1,6)
    if i==1:
        cara1+=1
    elif i==2:
        cara2+=1
    elif i==3:
        cara3+=1
    elif i==4:
        cara4+=1
    elif i==5:
        cara5+=1
    else:
        cara6+=1
print(f"*"*cara1+" cara de la 1" )
print(f"*"*cara2+" cara de la 2" )
print(f"*"*cara3+" cara de la 3" )
print(f"*"*cara4+" cara de la 4" )
print(f"*"*cara5+" cara de la 5" )
print(f"*"*cara6+" cara de la 6" )

# ejercicio 4
n=int(input("Dígite un número: "))
fact=1
for i in range(1,n+1):
    fact=fact*i 
print(f"El factorial de {n} es {fact}")