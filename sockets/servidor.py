import socket 
import threading
import sys
import pickle
import os

class Servidor():
    def __init__(self, host="localhost", port=7000):
        #arreglo para guardar los clientes conectados
        self.clientes = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((str(host), int(port)))
        self.sock.listen(1)
        self.sock.setblocking(False)

        #hilos para aceptar y procesar las conexiones
        aceptar = threading.Thread(target=self.aceptarCon)
        procesarls = threading.Thread(target=self.procesarListDir)
        aceptar.daemon = True 
        aceptar.start()
        procesarls.daemon = True
        procesarls.start()

        try:
            while True:
                msg = input('-> ')
                if msg == 'salir':
                    break
            self.sock.close()
            sys.exit()
        except:
            self.sock.close()
            sys.exit()

    def ls_to_client(self, cliente):
        try:
            print('entre a ls_to_client')
            path = '/home/liquid/workspace/backenduno/sockets/files'
            files_list = os.listdir(path)
            data = pickle.dumps(files_list)
            for c in self.clientes:
                if c == cliente:
                    c.send(data)
        except:
            print('error')
            cliente.close()

    def aceptarCon(self):
        print("aceptarCon aceptado")
        while True:
            try:
                conn, addr = self.sock.accept()
                conn.setblocking(False)
                self.clientes.append(conn)
                print(conn)
                print('nuevo cliente')
            except:
                pass
    
    def handleClient(self, c):
        while True:
            try:
                data = c.recv(1024)
                if data:
                    print(f'datos: {data.decode()}')
                else:
                    break
            except ConnectionResetError:
                print('el cliente c jue')
                break
        c.close()

    def procesarListDir(self):
        print('procesarListDir iniciado')
        while True:
            try:
                if len(self.clientes) > 0:
                    for c in self.clientes:
                        self.handleClient(c)
            except:
                pass

server = Servidor()
server()
