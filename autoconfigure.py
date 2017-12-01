"""
Author by SmallCrazyFrog
Email:ccieboy@msn.cn
thie is a autoconfigure script,if your are implteing wlan project ,
you can get the configure of acess control.
"""
import csv
#open a txt to store the configure
warning = """
*******************************************************************
                Notice    Very important 
Plaase give the ap file,the format of the file must be CSV,
also the path must be absolute path.
for example(C:\myap.csv);

Plaase give the output file,the format of the file must be txt,
also the path must be absolute path.
for example(C:\goodap.txt)
*******************************************************************
"""
print("\033[1;32;40m{warning}\033[0m".format(warning=warning))
apfile =input("\033[1;32;40m Plaase give the ap file:\033[0m")
outputfile = input("\033[1;32;40m Plaase give the output file:\033[0m")
if apfile[-4:] ==".csv" and outputfile[-4:] == ".txt":
    f =open(outputfile,"a")
#open a csv of access point and read the content
    with open(apfile, newline='') as csvfile:
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
        goodnews ="""
*******************************************************************
                         Congratulations! 
                      Codeing make life better!
               About Project:github.com/SmallCrazyFrog
*******************************************************************  
      """
    print("\033[1;32;40m{goodnews}\033[0m".format(goodnews=goodnews))
else:
    print("the ap file or outputfile is wrong. please check it!")



