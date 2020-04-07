#Q1 List and it default methods and functions
#append(X)
a = ["amruta", "yogita"]
print(a)
a.append("srushti")#Adds an item (x i.e srushti) to the end of the list.
print(a)

#extend([x,y])
a.extend(["srushti S", "alisha"])#Extends the list by appending all the items from the iterable. This allows you to join two lists together.
print(a)
#insert(index,value)
a.insert(0, "amru")#Inserts an item at a given position. The first argument is the index of the element before which to insert.
print(a)
a.insert(2, "yogi")
print(a)
#remove(value)
a.remove("amruta")#Removes the first item from the list that has a value of x. Returns an error if there is no such item.
print(a)
#pop()
# Example 1: No index specified
a.pop()
print(a)#Removes the item at the given position in the list, and returns it.  last item in the list.

# Example 2: Index specified
a.pop(1)#If no index is specified, pop() removes and returns the
print(a)
#clear
a.clear()
print(a)
#index()
a = ["amruta", "yogita","yogi","amru"]
print(a.index("amru"))
print(a.index("yogi", 2))#Returns the position of the first list item that has a value of x. Raises a ValueError if there is no such item.
#count() Returns the number of times x appears in the list
print(a.count("amru"))
print(a.count("yogi"))
print(a.count(""))
#sort(key=None, reverse=False) :Sorts the items of the list in place.


a.sort()
print(a)


a.sort(reverse=True)
print(a)

a.sort()
print(a)

a.sort(key=len)
print(a)

a.sort(key=len, reverse=True)
print(a)
#reverse() Reverses the elements of the list in place.
a.reverse()
print(a)
#copy():Returns a shallow copy of the list.
b = a.copy()
b.append("mumma")
print(a)
print(b)
#len(s):Returns the number of items in the list.
print(len(a))
#list([iterable]) :The list() constructor returns a mutable sequence list of elements.
print(list())
print(list([]))
print(list(["amruta","yogita","amru","yogi","srush"]))
print(list([["amru", "yogi"], ["amru"]]))

a = "amruta"
print(list(a))

a = ("I", "am", "a")
print(list(a))

a = {"I", "am", "a", "set"}
print(list(a))
#max(iterable, *[, key, default]) :Returns the largest item in an iterable (eg, list) or the largest of two or more arguments.
a = ["amru", "yogita", "amruta"]
print(max(a))

a = ["yogita", "yogi", "amruta"]
print(max(a))

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4]
print(max(a, b))
#min(iterable, *[, key, default]):Returns the smallest item in an iterable (eg, list) or the smallest of two or more arguments.
a = ["yogita", "yogi", "amruta"]
print(min(a))

a = ["yogita", "yogi", "amruta"]
print(min(a))

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4]
print(min(a, b))
#range(stop):Represents an immutable sequence of numbers and is commonly used for looping a specific number of times in for loops.
print(list(range(10)))
print(list(range(1,11)))
print(list(range(51,56)))
print(list(range(1,11,2)))


#Q2 Dictionary and its functions
#clear():Removes all the elements from the dictionary
alpha = {
  "a": "apple",
  "b": "banana",
  "c": "cat"
}
alpha.clear()
print(alpha)
#copy():	Returns a copy of the dictionary
alpha = {
  "a": "apple",
  "b": "banana",
  "c": "cat"
}
x = alpha.copy()
print(x)
#fromkeys()	Returns a dictionary with the specified keys and value
x = ('key1', 'key2', 'key3')
y = 1
thisdict = dict.fromkeys(x, y)
print(thisdict)
#get()	:Returns the value of the specified key
alpha = {
  "a": "apple",
  "b": "banana",
  "c": "cat"
}
x = alpha.get("apple")
print(x)
#items()	:Returns a list containing a tuple for each key value pair
x = alpha.items()
print(x)
#keys()	:Returns a list containing the dictionary's keys
x = alpha.keys()
print(x)
#pop()	:Removes the element with the specified key
alpha.pop("a")
print(alpha)
#popitem()	:Removes the last inserted key-value pair
alpha.popitem()
print(alpha)
#setdefault():Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
x = alpha.setdefault("c", "cat")
print(alpha)
#update():Updates the dictionary with the specified key-value pairs
alpha.update({"color": "White"})
print(alpha)
#values():Returns a list of all the values in the dictionary
x = alpha.values()
print(x)
#Q3 Set and its default functions
#add()	:Adds an element to the set
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
#clear():Removes all the elements from the set
fruits.clear()
print(fruits)
#copy()	:Returns a copy of the set
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)
#difference():Returns a set containing the difference between two or more sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)
#difference_update() :Removes the items in this set that are also included in another, specified set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)
#discard()	:Remove the specified item
fruits.discard("banana")
print(fruits)
#intersection()	:Returns a set, that is the intersection of two other sets
z = x.intersection(y)
print(z)#returns empty because no similar item is present
#intersection_update()	Removes the items in this set that are not present in other, specified set(s)
x.intersection_update(y)
print(x)
#isdisjoint()	Returns whether two sets have a intersection or not
z = x.isdisjoint(y)
print(z)
#issubset()	Returns whether another set contains this set or not
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)
#issuperset()	Returns whether this set contains another set or not
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)
#pop()	Removes an element from the set
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)
#remove()	Removes the specified element
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)
#symmetric_difference()	Returns a set with the symmetric differences of two sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
#symmetric_difference_update()	inserts the symmetric differences from this set and another
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
#union()	Return a set containing the union of sets
z = x.union(y)
print(z)
#update()	Update the set with the union of this set and others
x.update(y)
print(x)

