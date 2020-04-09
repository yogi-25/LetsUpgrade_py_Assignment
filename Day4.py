#Q Guessing Team India 2020 score cricket
import random as r
gen_score=r.randint(1,250)
print(gen_score)
user_score=int(input("enter your score"))
print(user_score)
type(user_score)
if user_score>250 and user_score<1:
    print("Reduce your expectation")
else:
    print("Ok to continue")
check_ran=gen_score-user_score
abs(check_ran)
if check_ran<=10 and check_ran>=1:
    print ("you are true india fan")
else:
    print("you are not true india fan")

#Q File assignment
file1=open("fle1.txt",'w')
file1.write("I love FCS")
file1.close()
file1=open("fle1.txt",'r')
print(file1.read())
