#realizar el codigo de cesar

#cesarscrypt

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

#entrada: input o en variable
text = input("Escribe un texto: ")
text = text.lower() #convertir el texto a minúsculas
#posiciones
posiciones = int(input("Posiciones de desplazamiento: "))

for n in text:
    if n in alfabeto:
        print(n, end="")
    else:
        alfabeto+=n

