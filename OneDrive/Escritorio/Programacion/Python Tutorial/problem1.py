#If we list all the natural numbers below  that are multiples of  or , we get  and . The sum of these multiples is .
import math
#Find the sum of all the multiples of  or  below

def problem0():
    numbers = []
    for num in range(1,454000):
        if math.sqrt(num)%2 == 0:
            numbers.append(num)
    result = sum(numbers)
    return result

def problem1():
    numbers = []
    for num in range(3,1000):
        if num %3 == 0 or num%5 == 0:
            numbers.append(num)
    result = sum(numbers)
    return result

#largest prime factor

def problem3():
    n = 600851475143
    largestNumber = 0
    for num in range(2,int(n **0.5)+1): 
        if n%num== 0:
            while n % num == 0:
                n //=num
                largestNumber = num
    if n > 1:
        largestNumber = n
    return largestNumber



#encontrar palíndromo de dos números de 3 dígitos
def problem4():
    n1 = 1
    n2 = 1
    for n in range(1,1000):
        n1+=1
        n2+=1
        result = n1*n2
        cadena = str(result)
        if cadena == cadena[::-1]:
            print("Encontrado: ",result)
            print("Valor n1: ",n1)
            print("Valor n2: ",n2)
            print(str(n1)+"x"+str(n2))


def problem6():
    #suma de el cuadrado de los primeros 100 numeros naturales+
    resultadoSuma = 0
    for n in range(1,101):
        n = n**2
        resultadoSuma+=n
    #la raiz cuadrada de la suma de los 100 numeros naturales
    resultadoRaiz = 0
    for n in range(1,101):
        resultadoRaiz+=n
    resultadoRaiz = resultadoRaiz **2 #elevamos al cuadrado
    #diferencia
    result = resultadoSuma - resultadoRaiz
    return result
print("Problema 6: ",problem6())


def fibonachi_problem():
    a = 0
    b = 1
    suma = 0 #inicializamos el resultado de suma
    while (a+b) < 4000000:
        c = a+b
        a = b
        b = c
        if c%2==0:
            suma+=c #actualizamos la suma
    print(suma)

problem4()