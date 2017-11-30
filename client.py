import socket
from time import sleep

manu = ''

s = socket.socket()

host = '127.0.0.1'
port = 12345

s.connect((host, port))

one = s.recv(1024).decode()
print(one)
two = s.recv(1024).decode()
print(two)
three = s.recv(1024).decode()
while manu != 3:
    manu = input(three)
    if manu == '1' or manu == '2':
        s.send(str(manu).encode())
        break
    print("Please select 1 or 2..")
    sleep(1)
four = s.recv(1024).decode()
if four == "You select to hold":
    print(four)
else:
    print("You're now holding ", four)

five = s.recv(1024).decode()
if five != 'you lose':
    print('let the computer think for an hour....')
    sleep(2)
    print("computer now have ", five)
    six = s.recv(1024).decode()
    print(six)
else:
    print(five)

s.close()