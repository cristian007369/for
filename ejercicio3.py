# ejercicio 3_simular el lanzamiento de n dados, e imprimir cuantas veces cayo cada cara . mostrar resultado con barras y asteriscos 
import random
#Se declaran seis variables para almacenar las veces que cae cada cara 
#También se pide el número de veces que sera lanzado el dado
cara1 , cara2 ,cara3 ,cara4 ,cara5 ,cara6=0 ,0 ,0 ,0 ,0 ,0 
lanzamiento=int(input("Dígite cuantas veces se va a lanzar el dado: "))

#Processing
for i in range(lanzamiento):
    dado=random.randint(1,6)
    if dado==1:
        cara1+=1
    elif dado==2:
        cara2+=1
    elif dado==3:
        cara3+=1
    elif dado==4:
        cara4+=1
    elif dado==5:
        cara5+=1
    else:
        cara6+=1

#Output
print(f"*"*cara1+" cara de lado 1" )
print(f"*"*cara2+" cara de lado 2" )
print(f"*"*cara3+" cara de lado 3" )
print(f"*"*cara4+" cara de lado 4" )
print(f"*"*cara5+" cara de lado 5" )
print(f"*"*cara6+" cara de lado 6" )