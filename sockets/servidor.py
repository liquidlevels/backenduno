import socket 
import threading
import sys
import pickle
import os
import shutil

class Servidor():
    def __init__(self, host="localhost", port=7000):
        #arreglo para guardar los clientes conectados
        self.clientes = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((str(host), int(port)))
        self.sock.listen(10)
        self.sock.setblocking(False)

        #hilos para aceptar y procesar las conexiones
        aceptar = threading.Thread(target=self.aceptarCon)
        procesar = threading.Thread(target=self.procesarCon)
        aceptar.daemon = True 
        aceptar.start()
        procesar.daemon = True 
        procesar.start()

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

    def msg_to_all(self, msg, cliente):
        for c in self.clientes:
            try:
                if c != cliente:
                    c.send(msg)
            except:
                self.clientes.remove(c)

    def aceptarCon(self):
        print("aceptarCon aceptado")
        while True:
            try:
                conn, addr = self.sock.accept()
                conn.setblocking(False)
                self.clientes.append(conn)
            except:
                pass
    
    def procesarCon(self):
        print("procesarCon iniciado")
        while True:
            if len(self.clientes) > 0:
                for c in self.clientes:
                    try:
                        data = c.recv(1024)
                        if data:
                            message = pickle.loads(data)
                            if message.startswith("ls"):
                                self.lsToClient(c)
                            elif message.startswith("get"):
                                self.getFileToClient(message, c)
                            else:
                                self.msg_to_all(data,c)
                    except:
                        pass
    
    def lsToClient(self, client):
        path = os.path.join(os.getcwd(), 'files')
        #path = "/home/liquid/workspace/backenduno/sockets/files"
        list_dir = os.listdir(path)
        response = "dir: " + ",".join(list_dir)
        try:
            client.send(pickle.dumps(response))
        except:
            print("no se pudo krnalgas")

    def getFileToClient(self, message, client):
        file = message.split()
        current_directory = os.getcwd()
        new_directory_path = os.path.join(current_directory, 'Downloads')

        if not os.path.exists(new_directory_path):
            os.mkdir(new_directory_path)
        
        path = os.path.join(current_directory,'files', file[1])
        pa_donde_lo_llevamos = os.path.join(new_directory_path, os.path.basename(path))
        
        try:
            shutil.copy(path, pa_donde_lo_llevamos)
            client.send(pickle.dumps("jalo, ve a: "+new_directory_path))
        except:
            client.send(pickle.dumps("no se pudo obtener el archivo"))

server = Servidor()
server()

