from math import factorial

num = 8
result = factorial(num)
print("Result: ",result)
#Función: empieza con def

def fac(num):
    res= 1
    while num >=1:
        res= res*num
        num = num -1
    return (res) #retornar resultado

x = fac(2)
y = fac(10)
promedio = (x + y) /2
print("Promedio: ",promedio)