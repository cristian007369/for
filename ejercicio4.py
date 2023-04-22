# ejercicio 4_calcular y mostrar el factorial de un número 
#Input
n=int(input("Dígite un número: "))
fact=1

#Processing
for i in range(1,n+1):
    fact*=i 

#Output
print(f"El factorial de {n} es {fact}")