frase = input("dame el mensaje a transmitir: ")
print("frase: ",frase)
mensaje = list(frase.replace(" ",""))
print(mensaje)

#TODO: hacer el encriptado y desecriptado de la frase con XOR
key = input("Dame la llave elegida: ")  
cifrado = [] #donde guardamos el cifrado
for i in mensaje:
    x = ord(i) ^ ord(key)
    cifrado.append(hex(x)) #añadimos la letra cifrada a la lista
print("Texto cifrado: ","".join(cifrado))