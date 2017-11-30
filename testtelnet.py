import sys
import os
import telnetlib
HOST = "192.168.1.224"
return1 =str((os.system('ping -n 1 -w 1 %s' % HOST)))
print(return1)
"""
user = input("Enter your remote account: ")
password = input("Enter your passowrd:")
tn = telnetlib.Telnet(HOST)
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
tn.write(b"display version\n")
print(tn.read_all().decode('ascii'))
"""