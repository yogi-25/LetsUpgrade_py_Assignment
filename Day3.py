#Q.WAP write a program to identify [1,1,5] in the given list in the same order if yes then print its match else its gone
# Python code find whether a list
# exists in list of list.
import collections

# Input List Initialization
Input = [[1, 1, 1, 2], [2, 3, 4], [1, 2, 3], [4, 5, 6]]

# List to be searched
list_search = [1,1,5]

# Flag initialization
flag = 0

# Using Counter
for elem in Input:
    if collections.Counter(elem) == collections.Counter(list_search):
        flag = 1

# Check whether list exists or not.
if flag == 0:
    print("its gone")
else:
    print("its match")


x = list(map(int, input("Enter a values: ").split()))
print("List of numbers is: ", x)
list_search = [1,1,5]
if any(list == list_search for list in x): # Using any to find whether list exists or not
    print("it's Match")
else:
    print("its Gone")
#result = any(elem in x for elem in list_search)
#if result:
#  print("it's Match")
#else:
    #print("its Gone")'''# Python3 code to demonstrate
# to check if list is subset of other
# using all()

# initializing list
test_list = [9, 4, 5, 8, 10]
sub_list = [1,1,5]

# printing original lists
print ("Original list : " + str(test_list))
print ("Original sub list : " + str(sub_list))

# using all() to
# check subset of list
flag = 0
if(all(x in test_list for x in sub_list)):
    flag = 1

# printing result
if (flag) :
    print ("its match")
else :
    print ("its gone")

# Python3 code to demonstrate
# to check if list is subset of other

# Importing
from collections import Counter


def checkInFirst(a, b):
    # getting count
    count_a = Counter(a)
    count_b = Counter(b)

    # checking if element exsists in second list
    for key in count_b:
        if key not in count_a:
            return False
        if count_b[key] > count_b[key]:
            return False
    return True


# initializing list
a = list(map(int, input("Enter a values: ").split()))
b = [1, 1,5]

# Calling function
res = checkInFirst(a, b)

# Printing list
print ("Original list : " + str(a))
print ("Original sub list : " + str(b))

if res == True:
    print ("its match")
else:
    print ("its gone")
