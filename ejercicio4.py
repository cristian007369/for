# ejercicio 4_calcular y mostrar el factorial de un número 
n=int(input("Dígite un número: "))
fact=1
for i in range(1,n+1):
    fact=fact*i 
print(f"El factorial de {n} es {fact}")