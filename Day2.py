#WAP for taking one number a input and then using if elif else concept,assign a grade to the input number from A,B,C,D,E Fail.
n=int(input("Enter a marks"))
if(n<=100):
 if(n>=85 and n<=100):
     print("A")
 elif(n>=75 and n<=84):
     print("B")
 elif(n>=65 and n<=74):
     print("C")
 elif(n>=45 and n<=64):
     print("D")
 elif(n>=35 and n<=44):
     print("E")
 else:
     print("FAIL")
else:
    print("You entered wrong choice")