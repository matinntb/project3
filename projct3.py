import re
class checkregister:
    def __init__(self,name,lastname,username,password,email,mobile,code):
        self.name=name
        self.lastname=lastname
        self.username=username
        self.password=password
        self.email=email
        self.mobile=mobile
        self.code=code
    
    def checkname(self):
        if re.match("[a-zA-Z\s]{2,20}$",name):      #checking name that just conclude latin and length of name should be between 1 and 20
            return True
        else:
            return False
    def checklastname(self):
        if re.match("[a-zA-Z\s]{2,30}$",lastname):  #checking lastname that just conclude latin and length should be between 1 and 30
            return True
        else:
            return False
    def checkusername(self):                        #checking username that just conclude latin and length should be between 6 and 50,be concluded @ and _.it can't be concluded space
        if re.match("^[a-zA-Z0-9_@\S]{7,50}$",username) and username.lower()!="username" and username.lower()!="admin":
            return True
        else:
            return False
    def checkpassword(self):                        #checking password that just conclude latin and length should be between 8 and 50,be concluded @,_,#,$,%,&.it can't be concluded space.in addition it shouldn't be easy
        if re.match("(?=.*\d)(?=.*[a-zA-Z])(?=.*[@_&#$%]){8,50}",password):
            return True
        else:
            return False
    def checkemail(self):                           #checking email
        if re.match("[\w\d.]+@[\w.]+\.[a-zA-Z]",email):
                return True
        else:
            return False
    def checkmobile(self):                          #checking mobileNumber that just conclude number and length of that is 11
        if re.match("[\d]{11}$",mobile):
            return True
        else:
            return False
    def checkcode(self):                            #checking code that just conclude number and length of that is 10 and other rules
        location=10
        summ=0
        mod=0
        if re.match("[\d]{10}$",code):
            for i in range(0,9):
                if code=='0000000000':
                    return False
                else:
                    summ+=int(code[i])*location
                    location-=1
                mod=summ%11
            if mod<2:
                if int(code[9])==mod:
                    return True
            else:
                if int(code[9])==11-mod:
                    return True
                else:
                    return False
        



name=""                                         #crearing variable
lastname=""
username=""
password=""
email=""
mobile=""
code=""

x=checkregister(name,lastname,username,password,email,mobile,code)      #crearing object
while True: 
    name=input("Enter your name:")
    if x.checkname()==True:
       pass
    else:
        print("***NAME ERROR*** ::: name just contain latins and space and number of character between 2 and 20")
        print("Register Error")
        break
    lastname=input("Enter your lastname:")
    if x.checklastname()==True:
       pass
    else:
        print("***LASTNAME ERROR***:::lastname just contain latins and space and number of character between 2 and 30")
        print("Register Error")
        break
    username=input("Enter your username:")
    if x.checkusername()==True :
        pass
    else:
        print("***USERNAME ERROR***:::Username just contain latins and number and @ ,_ . you don't have to use admin or username and space")
        print("Register Error")
        break
    password=input("Enter your password:")
    if x.checkpassword()==True:
        pass
    else:
        print("***PASSWORD ERROR***:::Password is to easy ")
        print("Register Error")
        break
    email=input("Enter your Email:")
    if x.checkemail()==True:
        pass
    else:
        print("***EMAIL ERROR***:::Email should be like a@b.com")
        print("Register Error")
        break
    mobile=input("Enter your mobileNumber:")
    if x.checkmobile()==True:
        pass
    else:
        print("***MOBILE NUMBER ERROR***:::Mobile Number has 11 charachter and just number")
        print("Register Error")
        break
    code=input("Enter your Code:")
    if x.checkcode()==True:
        pass
    else:
        print("***CODE ERROR***:::Code shoule be 11 character and just contain number and it is True in rule")
        print("Register Error")
        break
    print("Register ok")
    break


