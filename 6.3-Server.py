import socket
import sys
import math
import errno
import time
from multiprocessing import Process

ok_message = 'HTTP/1.0 200 OK\n\n'
nok_message = 'HTTP/1.0 404 Not Found\n\n'

def ProcessStart(server):
     while True:
            ch = server.recv(1024).decode()

            if ch == '1':
                #log function
                numb = server.recv(1024).decode()
                calc = math.log(float(numb))

            elif ch  == '2':
                #square Root funtion
                numb = server.recv(1024).decode()
                calc = math.sqrt(float(numb))

            elif ch  == '3':
                #exponential funtion
                numb = server.recv(1024).decode()
                calc = math.exp(float(numb))

            elif ch == '9':
                server.close()
                break

            server.sendall(str(calc).encode())

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind(('',8888))

    except socket.error as e:
        print (str(e))
        sys.exit()

    s.listen(3)
    while True:
        try:
            server, addr = s.accept()
            print ('\nConnected!')
            p = Process(target = ProcessStart, args=(server,))
            p.start()

        except socket.error:
            print ('There is a socket error')

    s.close()
