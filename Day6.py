str1=input("Enter the text")
c=0
H1=["A", "D", "O", "P", "R",'Q'] #incremate by 1
H2=["B"]#incremates  count by 2
for i in str1:
    if i in H1:
       c=c+1
    elif i in H2:
        c=c+2
print(c)
