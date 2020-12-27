import socket 
import sys

Client = socket.socket()
try:
    Client.connect(('192.168.0.163',8888))
    print ('Connected!')
except socket.error as e:
    print ( str(e) )

loop = True

while loop:
    print ('\n Mathmatical functions in python')
    print (' 1. Logarithmic (Log)')
    print (' 2. Square Root')
    print (' 3. Exponential function')
    print (' 9. Exit')
    
    ch = input ('\n Enter your choice : ' )
    Client.send(ch.encode())

    if ch == '1':
        print ('\n [+] Logarithmic Function ')
        numb = input ('\n Enter a number : ')
        Client.send(numb.encode())
        tot = Client.recv(1024)

        print ( ' Log('+ numb +') : ' + str(tot.decode()))

    elif ch == '2':
            print ('\n [+] Square Root Function ')
            numb = input ('\n Enter a number : ')
            if int(numb) > -1 :
                Client.send(numb.encode())
                tot = Client.recv(1024)
            else :
                print ('\n Square root is not a negative number!')

            print ( ' Square root for(' + numb +'): ' + str(tot.decode()))

    elif ch == '3':
        print ('\n [+] Exponential Function ')
        numb = input ('\n Enter a number : ')
        Client.send(numb.encode())
        tot = Client.recv(1024)

        print ( ' Exponential for (' + numb + '): ' + str(tot.decode()))

    elif ch == '9':
        Client.close()
        sys.exit()
    else:
        print ('\n Invalid input!')

    input ( '\n Press Enter to Continue .. ')
