#Q Complete notebook for map,filter,reduse and lambda
 #map()
#Python map()

'''function is used to apply a function on all the elements of specified iterable and return map object. Python map object is an iterator, so we can
iterate over its elements. We can also convert map object to sequence objects such as list, tuple etc.
using their factory functions.'''
#Python map() function syntax is:
   #map(function, iterable, ...)
''' We can pass multiple iterable arguments to map() function, in that case, the specified function must have that many arguments. The function will
     be applied to these iterable elements in parallel. With multiple iterable arguments, the map iterator stops when
      the shortest iterable is exhausted.'''


def to_upper_case(s):
    return str(s).upper()

def print_iterator(it):
    for x in it:
        print(x)
    print('')  # for new line

# map() with string
map_iterator = map(to_upper_case, 'abc')
print(type(map_iterator))
print_iterator(map_iterator)


# map() with tuple
map_iterator = map(to_upper_case, (1, 'a', 'abc'))
print_iterator(map_iterator)

#converting mp with list,tuple and set
map_iterator = map(to_upper_case, ['x', 'a', 'abc'])
print_iterator(map_iterator)


map_iterator = map(to_upper_case, ['a', 'b', 'c'])
my_list = list(map_iterator)
print(my_list)

map_iterator = map(to_upper_case, ['a', 'b', 'c'])
my_set = set(map_iterator)
print(my_set)

map_iterator = map(to_upper_case, ['a', 'b', 'c'])
my_tuple = tuple(map_iterator)
print(my_tuple)


#Python map() with lambda
#We can use lambda functions with map() if we don’t want to reuse it.
#This is useful when our function is small and we don’t want to define a new function.

list_numbers = [1, 2, 3, 4]

map_iterator = map(lambda x: x * 2, list_numbers)
print_iterator(map_iterator)


# map() with multiple iterable arguments
list_numbers = [1, 2, 3, 4]
tuple_numbers = (5, 6, 7, 8)
map_iterator = map(lambda x, y: x * y, list_numbers, tuple_numbers)
print_iterator(map_iterator)



# map() with multiple iterable arguments of different sizes
list_numbers = [1, 2, 3, 4]
tuple_numbers = (5, 6, 7, 8, 9, 10)
map_iterator = map(lambda x, y: x * y, list_numbers, tuple_numbers)
print_iterator(map_iterator)

map_iterator = map(lambda x, y: x * y, tuple_numbers, list_numbers)
print_iterator(map_iterator)


#map() with function None

map_iterator = map(None, 'abc')
print(map_iterator)
for x in map_iterator:
    print(x)


#lambda:lambda in python is used to create anonymous functions. Anonymous functions are those functions who are unnamed.
# That means you are defining a function without any name of the function.
#Syntax :
         #lambda arguments: expression

''' def functionName(arguments):
        statements...
        return something'''

def squareof(x):
   return x*x

p = squareof(5)
print(p)
#We can convert above function to python lambda function as follows:
f = lambda x: x*x
p = f(5)
print(p)
#Use of python lambda function in map()

numbers = [ 74, 85, 14, 23, 56, 31,44 ]

remainders = map(lambda num: num%5, numbers)
for i in remainders:
   print(i)


#filter() Function in python
#Python filter() function is used to filter the elements of an iterable based
#on a function. This function returns filter object that is an iterator.
#Syntax:
'''filter(function, iterable)
function will be called on iterable elements and if it returns True then they will be part of the returned iterator.




'''
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


def print_filter_items(my_filter):
    for item in my_filter:
        print(item)
    print()
 #Let’s use filter() function to get an iterator of
# even numbers only from the input iterable of integers. We will use tuple and list for our example, both of them are iterable.
l1 = [1, 2, 3, 4, 5]
fl = filter(is_even, l1)
print(type(fl))
print_filter_items(fl)

t = (1, 2, 3, 4, 5)
fl = filter(is_even, t)
print_filter_items(fl)

#Python filter() example with None function
t = (True, False, 1, 0, 0.0, 0.5, '', 'A', None)
fl = filter(None, t)
print_filter_items(fl)

'''Reduce function in python:
           The reduce(fun,seq) function is used to apply a particular function passed in its
            argument to all of the list elements mentioned in the sequence passed along.This function is defined 
            in “functools” module.
            '''
# python code to demonstrate working of reduce()

# importing functools for reduce()
import functools

# initializing list
lis = [ 1 , 3, 5, 6, 2, ]

# using reduce to compute sum of list
print ("The sum of the list elements is : ")
print (functools.reduce(lambda a,b : a+b,lis))

# using reduce to compute maximum element from list
print ("The maximum element of the list is : ")
print (functools.reduce(lambda a,b : a if a > b else b,lis))
'''reduce() can also be combined 
with operator functions to achieve the similar functionality as with lambda functions 
and makes the code more readable.'''
# python code to demonstrate working of reduce()
# using operator functions

# importing functools for reduce()
import functools

# importing operator for operator functions
import operator

# initializing list
lis = [ 1 , 3, 5, 6, 2, ]

# using reduce to compute sum of list
# using operator functions
print ("The sum of the list elements is : ")
print (functools.reduce(operator.add,lis))

# using reduce to compute product
# using operator functions
print ("The product of list elements is : ")
print (functools.reduce(operator.mul,lis))

# using reduce to concatenate string
print ("The concatenated product is : ")
print (functools.reduce(operator.add,["yes","i","got"]))
