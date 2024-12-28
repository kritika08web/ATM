

import mysql.connector as c
con=c.connect(host="localhost",user="root",password="Subhash15@",database="bank")
cursor=con.cursor()
if con.is_connected():
    print("susscessfully connected")
class bank:
    def __init__(self,__account_no,balance,name):
        self.__account_no=__account_no
        self.balance=balance
        self.name=name
        self.__current_password="bob"
    def password(self,__password):
        self.__password=__password
        if (self.__password==self.__current_password):
            return True
        else:
            return False
    def new_password(self,__new_password):
        self.__new_password=__new_password
        self.__current_password=__new_password
        print("Password successfully reset")
    def debit(self,debit_ammount):
        self.debit_ammount=debit_ammount
        if (self.balance<self.debit_ammount):
            print("Not sufficient balance")
        else:
            self.balance-=self.debit_ammount
            print("Ammount is successfully debited from your account: balance ammount:",self.balance)
    def credit(self,credit_ammount):
        self.credit_ammount=credit_ammount
        self.balance+=self.credit_ammount
        print("Ammount successfully credited in your account: balance ammount:",self.balance)
while True:
    __account_no=int(input("Enter your account no.:"))
    name=input("Enter the name of the user:")
    balance=float(input("Enter the balance ammount present in your account:"))
    user=bank(__account_no,balance,name)
    __password=input("Enter your account password:")
    if user.password(__password):
        print("Correct Password")
        query=" insert into user values({},'{}','{}',{})".format(__account_no,name,__password,balance)
        cursor.execute(query)
        con.commit()
        debit_ammount=input("Do you Want to debit an ammount? (yes/no):").strip().lower()
        if (debit_ammount=="yes"):
            debit_ammount=float(input("Enter the ammount to be debited:"))
            user.debit(debit_ammount)
            query2="insert into debit values({},{},{})".format(__account_no,debit_ammount,user.balance)
            cursor.execute(query2)
            con.commit()
        else:
            print("No ammount to be debited")
        credit_ammount=input("Do you Want to credit an ammount? (yes/no):").strip().lower()
        if (credit_ammount=="yes"):
            credit_ammount=float(input("Enter the ammount to be credited:"))
            user.credit(credit_ammount)
            
        else:
            print("NO ammount to be credited")
    else:
        print("Incorrect password")
        code=int(input("enter the code:"))
        if (code==2022):
            reset_choice=input("forget password ? (yes/no):").strip().lower()
            if (reset_choice=="yes"):
                __new_password=input("Create a new password:")
                user.new_password(__new_password)
                __account_no=int(input("Enter your account no.:"))
                user=bank(__account_no,balance,name)
                __password=input("Enter your account password:")
                user.password(__password)
                query=" insert into user values({},'{}','{}',{})".format(__account_no,name,__password,balance)
                cursor.execute(query)
                con.commit()
                debit_ammount=input("Do you Want to debit an ammount? (yes/no):").strip().lower()
                if (debit_ammount=="yes"):
                    debit_ammount=float(input("Enter the ammount to be debited:"))
                    user.debit(debit_ammount)
                    query2="insert into debit values({},{},{})".format(__account_no,debit_ammount,user.balance)
                    cursor.execute(query2)
                    con.commit()
                    
                else:
                    print("No ammount to be debited")
                credit_ammount=input("Do you Want to credit an ammount? (yes/no):").strip().lower()
                if (credit_ammount=="yes"):
                    credit_ammount=float(input("Enter the ammount to be credited:"))
                    user.credit(credit_ammount)
                    
                else:
                    print("NO ammount to be credited")
            else:
                print("Sorry you can not access the account")
        else:
            print("access denied")
    query3="insert into credit values ({},{},{})".format(__account_no,credit_ammount,user.balance)
    cursor.execute(query3)
    con.commit()
    x=int(input("1--->Enter More\n2--->Exit\n enter your choice"))
    if x==2:
        break
                      
        
