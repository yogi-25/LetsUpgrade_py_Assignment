# Python Program to find Sum of Digits of a Number using While Loop

'''no=input("enter the number")
i=-999999999
i=int(i)
for i in no:
    i=i+1
    print(no)
from array import *

array1 =input("enter")

for x in array1:
 x+=1
 print(x)'''


Number = int(input("Please Enter any Number: "))
Sum = 0

while(Number > 0):
    Reminder = Number % 10
    Sum = Sum + Reminder
    Number = Number //10

print("\n Sum of the digits of Given Number = %d" %Sum)