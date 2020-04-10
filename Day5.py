# PROBLEM STATEMENT 1 : Q. You have seen how powerful dictioary data stucture is In this assignment given a number n.You have to write a program that generate
# a dictinary d which contaion (i,i*i) where i  is from 1 to nTHen you have juct print that dictionary.
n=int(input("Enter a number:"))
d={x:x*x for x in range(1,n+1)}
print(d)

# PROBLEM STATEMENT 2: You have also seen how list slicing is performed in python .In this program create a list of numbers from
#from 1 to 50 named list_1 .The number shule be present from increaing order .i.e index zero should be 1 ,index one shoude be 2
#Given an input two numbers lets say a and b you have to print the numbers returned by the following command list_1[a:b]
#list_1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
list_1=[i for i in range(1,51)]
a=int(input())
b=int(input())
for s in range(a,b):
   print(s+1)
