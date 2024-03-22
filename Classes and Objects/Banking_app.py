
#task 1 loop n times ( n provided by user) create n object put it in alist
#task 2 take username and password form user chech which object it belong to 
#task 3 display all information of that user
#task 4 take username of pereson who you want to send money
#task 5 find the object with that user user name and deposit the required amount
#task 6 withdraw amount from your object and deposit to target object
import getpass

class bank_account:
    def __init__(self,name,address,balance,password):
        self.name=name
        self.address=address
        self.balance=balance
        self.password=password
    
    def printAll(self) -> None:
        print(f'Name:{self.name} \nAddress:{self.address} \nBalance:{self.balance}')
    
    def withdraw(self,amount) -> None:
        self.balance-=amount
    
    def deposit(self,amount) -> None:
        self.balance+=amount


accounts=[]
print('Welcome to our bank')
n=int(input('Enter the no of user to create account: '))
for i in range(0,n,1):
    name=input('Enter your name: ')
    address=input('Enter your address: ')
    balance=input('Enter your balance: ')
    password=getpass.getpass('Enter your password: ')
    accounts.append(bank_account(name,address,balance,password))

#Task 2 Authentication
flag=0
acc_name=input('Enter the account_name:')
Password=getpass.getpass('Enter your password: ')
for individualAcc in accounts:
    if individualAcc.name==acc_name and individualAcc.password==Password:
        print('User Found. \nPassword Matched ...')
        flag=1
    elif individualAcc.name==acc_name and individualAcc.password!=Password:
        # print('Incorrect Password')
        flag=2
if flag==1:
    print(f"The user info is given below:")
    individualAcc.printAll()
elif flag==2:
    print('Password not matched !!!')
elif flag ==0:
    print('Username not found')


