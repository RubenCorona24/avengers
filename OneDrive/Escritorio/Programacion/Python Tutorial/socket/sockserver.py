# Echo server program
import socket
import threading

# Función para encriptar y desencriptar
def cypher(texto, key):
    plano = list(texto)
    cifrado = []

    for i in plano:
        x = ord(i) ^ ord(key)
        cifrado.append(hex(x))

    return " ".join(cifrado)

def decypher(texto, key):
    cifrado = texto.split()
    plano = []

    for i in cifrado:
        x = int(i, 16) ^ ord(key)
        plano.append(chr(x))

    return "".join(plano)

def recibir(conn):
    while True:
        data = conn.recv(1024).decode()
        if not data:
            print("El cliente cerró la conexión")
            break
        print("\nRecibido:", decypher(data, 'k'))

HOST = "127.0.0.1"  # Symbolic name meaning the local host
PORT = 4448         # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)
print("Esperando conexión...")

conn, addr = s.accept()
print('Connected by', addr)

t = threading.Thread(target=recibir, args=(conn,))
t.daemon = True
t.start()

while True:
    mensaje = input("Mensaje a enviar: ")
    mensaje_cifrado = cypher(mensaje, 'k')
    conn.send(mensaje_cifrado.encode("utf-8"))