"""
this is a samll program, you can user id and password login,
if you have try three times ,your id will been locked>
"""
_username = "abc"
_password = "123"
counter =  0
while counter <3:
    username = input("Username:")
    readfile = open("C:\lock.txt")
    lockuser = readfile.readline()
    if lockuser == username:
        warning="""
        ++++++++++
        You has been locked!
        ++++++++++
        """
        print(warning)
    else:
        password = input("Password:")
        if _username == username and _password ==password:
            info="""
                +++++++++++++++++
                welcome to {name}
                +++++++++++++++++
                """.format(name=username)
            print(info)
            break
        else:
            counter = counter+1
            trylogin = 3 - counter
            helpinfo ="""
          Your username or password is wrong,please check your id and password! 
          if you try more than three times ,your id will been locked !
          you can try {trylogin} !
          """.format(trylogin = str(trylogin))
            print(helpinfo)
            if counter == 3:
                lock = open("C:\lock.txt","w")
                lock.write(username)
                lockwarning = """
                       ++++++++++
                       You will been locked!
                       ++++++++++
                       """
                print(lockwarning)


