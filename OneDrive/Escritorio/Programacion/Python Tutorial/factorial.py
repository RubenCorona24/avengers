#hacer un prog. en python que calcule el Factorial de un número sin IA

def factorizar(dato):
    res= 1
    while dato >=1:
        res = res * dato
        dato-=1
    return res

print(factorizar(6))
x = factorizar(4)
y = factorizar(6)
numeros = [x,y]
promedio = sum(numeros)/len(numeros)
print("Promedio: ",promedio)