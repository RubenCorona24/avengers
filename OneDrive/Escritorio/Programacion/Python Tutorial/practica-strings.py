alfabeto = 'abcdefghijklmnopqrstuvwxyz'

#funciones index y find: devuelven lo mismo
#En caso de error: find devuelve -1, index devuelve excepción

x = alfabeto.find("m")
y = alfabeto.index("m")
print(x)
print(y)
z = alfabeto.find("L")
print(z)
texto = "HeLlo World"
plano = texto.lower() #convertimos letras en minpusculas
print(plano)

#isaplha: función que dice si es alfanumérico => devuelve booleano
letter = "&"
print(letter.isalpha()) #false
