import random
import string

def get_random_string(lenght): #recibe el largo de la cadena
    letras = string.ascii_lowercase
    resultado = ''.join(random.choice(letras) for letra in range(lenght))
    print("Largo de la cadena: ",lenght)
    print("Cadena aleatoria: ",resultado)

get_random_string(3)
get_random_string(10)
