#XOR de python no funciona con strings
#para sacar el numero ascii de una letra es con ordinal (ord)

#ord: devuelve el valor decimal de la tabla ASCII
#devuelve un caracter

texto  = "h"
print(ord(texto))
key = 'k'

texto = ord(texto)
key = ord(key)

enc = texto ^ key
print(enc)

new_texto = chr(3)
print(new_texto)
texto = enc ^ key
print(chr(texto)) #desencriptar para obtener la h

