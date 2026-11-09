#importar os (sistema operativo)
import os

#Generar 2 bites aleatorios
x = os.urandom(2)

print(f"Bytes random: {x}")
print(f"Representación hexadecimal: {x.hex()}")
