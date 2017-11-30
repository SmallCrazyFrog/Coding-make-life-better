"""
this is a auto login program
"""
import telnetlib
f = open("C:\ip.txt")
line = f.readline()
ip = line.split(" ",3)[0]
user = line.split(" ",3)[1]
password = line.split(" ",3)[2]
command = "display version"
connect = telnetlib.Telnet(ip)
connect.read_until(b"Username:")
connect.write(user.encode("ascii") + b"\n")
connect.read_until(b"Password:")
connect.write(password.encode("ascii") + b"\n")
connect.read_until(b"<")
connect.write(command.encode("ascii")+ b"\n")
f.close()