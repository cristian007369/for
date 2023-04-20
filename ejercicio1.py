# ejercicio 1_Leer n número enteros mostrar cuantos son pares e impares 
#Input

n=int(input("Dígite un número: "))
num_pares=0
num_impares=0

#Processing
for i in range(1,n+1):
    if i%2==0:
        num_pares+=1
    else:
        num_impares+=1

#Output
print(f"Hay {num_pares} números pares en {n}")
print(f"Hay {num_impares} números impares en {n}")