# ejercicio 3_simular el lanzamiento de n dados, e imprimir cuantas veces cayo cada cara . mostrar resultado con barras y asteriscos 
import random
#Se declaran seis variables para almacenar las veces que cae cada cara 
#También se pide el número de veces que sera lanzado el dado
lanzamiento=int(input("Dígite cuantas veces se va a lanzar el dado: "))
cara1 = cara2 = cara3 = cara4 = cara5 = cara6=0 

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
print("*"*cara1+f" cara de lado 1, {cara1}\n" +
      "*"*cara2+f" cara de lado 2, {cara2}\n" +
      "*"*cara3+f" cara de lado 3, {cara3}\n" +
      "*"*cara4+f" cara de lado 4, {cara4}\n" +
      "*"*cara5+f" cara de lado 5, {cara5}\n" +
      "*"*cara6+f" cara de lado 6, {cara6}")