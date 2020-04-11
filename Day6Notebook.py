#Python map() function is used to apply a function on all the elements of specified iterable and return map object. Python map object is an iterator, so we can
# iterate over its elements. We can also convert map object to sequence objects such as list, tuple etc. using their factory functions.
#Python map() function syntax is:
   #map(function, iterable, ...)
''' We can pass multiple iterable arguments to map() function, in that case, the specified function must have that many arguments. The function will
     be applied to these iterable elements in parallel. With multiple iterable arguments, the map iterator stops when the shortest iterable is exhausted.'''


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

