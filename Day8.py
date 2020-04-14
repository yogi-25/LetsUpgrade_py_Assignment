
def check():
        try:
            D = int(input('\nPlease enter binary number: '), 2)
        except ValueError:
            print('Please make sure your number contains digits 0-1 only.')

        c=0
        while (D>-1):
         Reminder = D % 10
         if(Reminder==1 and Reminder==0):
              print("NO")
         return c

x=check()
if(x==0):
    print("YES")
