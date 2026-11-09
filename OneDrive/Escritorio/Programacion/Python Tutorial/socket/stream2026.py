def encdec(mensaje,key):
    salida = ''
    for l in mensaje:
        x = ord(l) ^ ord(key)
        salida += chr(x)
    return salida

mensaje = "Hola Mundo"
key = 'A'
cifrado = encdec(mensaje,key)
print("Mensaje cifrado", cifrado)
descifrado = encdec(cifrado,key)
print(descifrado)


