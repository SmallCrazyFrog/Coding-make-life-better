"""
Author by SmallCrazyFrog
Email:ccieboy@msn.cn
thie is a autoconfigure script,if your are implteing wlan project ,
you can get the configure of acess control.
"""
import csv
import re
#open a txt to store the configure
f =open("C:\goodap.txt","a")
#open a csv of access point and read the content
with open('C:\myap.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar=',')
    for row in spamreader:
        date=row[0]
        #spilte the param
        name =date.split(",")[0]
        modle = date.split(",")[2]
        serial = date.split(",")[1]
        #format the message
        msg ="""
       wlan ap {name} modle {modle}
       serial-no {serial}
       radio 1
       service-ter 1
       radio enable
       radio 2
       service-ter 1
       radio enable
        """.format(name=name,modle=modle,serial=serial)
        # it is the time to witness the miracle!
        f.write(msg)
print("good boy , well done!")



