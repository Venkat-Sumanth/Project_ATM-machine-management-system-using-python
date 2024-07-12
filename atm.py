username = 'sumanth'
password = 'python123'

c_name = input("Enter your name:")
c_pass = str(input("Enter your password"))
if c_name ==username and c_pass ==password:
    # print("success")
    print('''
    1.Deposite
    2.withdraw
    3.ministatement
    4.exit
    ''')
    amount=5000
    option=int(input('select your option:'))
    if option==1:
        dep=int(input('Enter your amount'))
        amount+=dep
        print("Total amount:", amount)
    elif option==2:
        withd=int(input('Enter the amount:'))
        amount-=withd
        print("Total amount:", amount)
    elif option==3:
        print('==========ATM============')
        print('Username:', username)
        print("Total amount:", amount)
        print('Thanks for visiting')
        print('==========================')
    elif option==4:
        print('Exit')
else:
    print("Please enter correct login")