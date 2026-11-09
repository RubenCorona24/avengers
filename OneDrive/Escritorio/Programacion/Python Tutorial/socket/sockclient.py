# Echo client program
import socket
import threading
import secrets # valores aleatorios seguros
import string

def generarLlave(longitud=16):
    alfabeto = string.ascii_letters + string.digits
    return "".join(secrets.choice(alfabeto) for _ in range(longitud))

def cypher(texto, key):
    cifrado = []

    for i,c in enumerate(texto):
        x = ord(c) ^ ord(key[i % len(key)])
        cifrado.append(hex(x))

    return " ".join(cifrado)

def decypher(texto, key):
    plano = []

    for i,h in enumerate(texto.split()):
        x = int(h, 16) ^ ord(key[i % len(key)])
        plano.append(chr(x))

    return "".join(plano)

def recibir(sock,key):
    while True:
        data = sock.recv(1024).decode()
        if not data:
            print("El servidor cerró la conexión")
            break
        print("\nRecibido:", decypher(data, key))

HOST = "127.0.0.1"  # The remote host
PORT = 4448         # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

KEY = s.recv(1024).decode()
print("Llave recibida: ",KEY)
t = threading.Thread(target=recibir, args=(s,KEY))
t.daemon = True
t.start()

while True:
    mensaje = input("Que quieres enviar: ")
    mensaje_cifrado = cypher(mensaje, KEY)
    s.send(mensaje_cifrado.encode("utf-8"))