import os
import re
import csv
conuter = 0
ipno = 0
serial = 1
modleno = 2
date =[]
f = open("C:\myap.txt")
gooddate = open("C:\goodap.txt","a")
while 1:
    line = f.readline()
    if not line:
        break
        print("it is a bad news")
    pass
    newcontenet = re.split(" ",line)
    name=newcontenet[ipno]
    serialno=newcontenet[serial]
    modle=newcontenet[modleno]
    msg = """
    wlan ap {name} model {model}
    serial-no {serialno}
    radio 1
    service-te 1
    radio 2
    service-te 1
    """.format(name=name,serialno=serialno,model=modle)
    gooddate.write(msg)
print("well done")

