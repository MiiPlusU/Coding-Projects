#!/usr/bin/python


# The range() function can also modify it's 3 defaults arguments. The first two will be the start and stop values, and the third will be the step argument. The step is the amount that the variable is increased by after each iteration.
# The range() function returns a sequence of numbers. It starts from 0, increments by 1, and stops before a specified number:
# last number in range is not included
# import sys sys.exit() exits program

def say_hi(name, greeting):
	print(f"{greeting} {name}")
	
# without keyword arguments
say_hi('John', 'Hello')
# Hello John

# with keyword arguments
say_hi(name='Anna', greeting='Hi')
# Hi Anna

def add(x, y):
    return x + y
    add(5, 3)
# 8

def make_adder(n):
    return lambda x: x + n
plus_3 = make_adder(3)
plus_5 = make_adder(5)
plus_3(4)
# 7
plus_5(4)
# 9

# [0:2] 2nd index not included


spam2 = spam[:]
# ['cat', 'bat', 'rat', 'elephant']
spam.append('dog')
spam
# ['cat', 'bat', 'rat', 'elephant', 'dog']
spam2
# ['cat', 'bat', 'rat', 'elephant']

furniture = ['table', 'chair', 'rack', 'shelf']
len(furniture)
# 4



#Changing values with indexes
furniture = ['table', 'chair', 'rack', 'shelf']

furniture[0] = 'desk'
furniture
# ['desk', 'chair', 'rack', 'shelf']

furniture[2] = furniture[1]
furniture
# ['desk', 'chair', 'chair', 'shelf']

furniture[-1] = 'bed'
furniture
# ['desk', 'chair', 'chair', 'bed']




#Concatenation and Replication
[1, 2, 3] + ['A', 'B', 'C']
# [1, 2, 3, 'A', 'B', 'C']

['X', 'Y', 'Z'] * 3
# ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']

my_list = [1, 2, 3]
my_list = my_list + ['A', 'B', 'C']
my_list
# [1, 2, 3, 'A', 'B', 'C']






# Getting the index in a loop with enumerate()
furniture = ['table', 'chair', 'rack', 'shelf']

for index, item in enumerate(furniture):
    print(f'index: {index} - item: {item}')
# index: 0 - item: table
# index: 1 - item: chair
# index: 2 - item: rack
# index: 3 - item: shelf




#Loop in Multiple Lists with zip()
furniture = ['table', 'chair', 'rack', 'shelf']
price = [100, 50, 80, 40]
#zip function packs the tuple, you have to use the tuple() function to unpack its

for item, amount in zip(furniture, price):
    print(f'The {item} costs ${amount}')
# The table costs $100
# The chair costs $50
# The rack costs $80
# The shelf costs $40





#The in and not in operators
'rack' in ['table', 'chair', 'rack', 'shelf']
# True
'bed' in ['table', 'chair', 'rack', 'shelf']
# False
'bed' not in furniture
# True
'rack' not in furniture
# False



#The Multiple Assignment Trick
furniture = ['table', 'chair', 'rack', 'shelf']
table, chair, rack, shelf = furniture
table
# 'table'
chair
# 'chair'
rack
# 'rack'
shelf
# 'shelf'

a, b = 'table', 'chair'
a, b = b, a
print(a)
# chair
print(b)
# table







#The index Method
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.index('chair')
# 1








# Adding Values
### append()
# append adds an element to the end of a list:
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.append('bed')
furniture
# ['table', 'chair', 'rack', 'shelf', 'bed']

# insert()
# insert adds an element to a list at a given position:
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.insert(1, 'bed')
furniture
# ['table', 'bed', 'chair', 'rack', 'shelf']


# Removing Values
# del()
# del removes an item using the index:
furniture = ['table', 'chair', 'rack', 'shelf']
del furniture[2]
furniture
# ['table', 'chair', 'shelf']

del furniture[2]
furniture
# ['table', 'chair']


# remove()
# remove removes an item with using actual value of it:
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.remove('chair')
furniture
# ['table', 'rack', 'shelf']


# pop()
# By default, pop will remove and return the last item of the list. You can also pass the index of the element as an optional parameter:
animals = ['cat', 'bat', 'rat', 'elephant']
animals.pop()
'elephant'
animals
['cat', 'bat', 'rat']
animals.pop(0)
'cat'
animals
['bat', 'rat']







# Sorting values with sort()
numbers = [2, 5, 3.14, 1, -7]
numbers.sort()
numbers
# [-7, 1, 2, 3.14, 5]

furniture = ['table', 'chair', 'rack', 'shelf']
furniture.sort()
furniture
# ['chair', 'rack', 'shelf', 'table']

furniture.sort(reverse=True)
furniture
# ['table', 'shelf', 'rack', 'chair']

letters = ['a', 'z', 'A', 'Z']
letters.sort(key=str.lower)
letters
# ['a', 'A', 'z', 'Z']

furniture = ['table', 'chair', 'rack', 'shelf']
sorted(furniture)
# ['chair', 'rack', 'shelf', 'table']

# The Tuple data type
# Tuples vs Lists The key difference between tuples and lists is that, while tuples are immutable objects, lists are mutable. This means that tuples cannot be changed while the lists can be modified. Tuples are more memory efficient than the lists.
furniture = ('table', 'chair', 'rack', 'shelf')

furniture[0]
# 'table'

furniture[1:3]
# ('chair', 'rack')

len(furniture)
# 4






# Converting between list() and tuple()
tuple(['cat', 'dog', 5])
# ('cat', 'dog', 5)

list(('cat', 'dog', 5))
# ['cat', 'dog', 5]

list('hello')
# ['h', 'e', 'l', 'l', 'o']









# Local and Global Scope

global_variable = 'I am available everywhere'

def some_function():
print(global_variable)  # because is global
local_variable = "only available within this function"
print(local_variable)

# the following code will trow error because
# 'local_variable' only exists inside 'some_function'
print(local_variable)
Traceback (most recent call last):
  File "<stdin>", line 10, in <module>
NameError: name 'local_variable' is not defined

def spam():
    global eggs
    eggs = 'spam'

    eggs = 'global'
    spam()
    print(eggs)







# Python Dictionaries
    my_cat = {
    'size': 'fat',
    'color': 'gray',
    'disposition': 'loud'
    }
# values()
pet = {'color': 'red', 'age': 42}
for value in pet.values():
    print(value)
# red
# 42

# keys()
pet = {'color': 'red', 'age': 42}
for key in pet.keys():
    print(key)
# color
# age

# items()
pet = {'color': 'red', 'age': 42}
for item in pet.items():
    print(item)
# ('color', 'red')
# ('age', 42)

# get()
wife = {'name': 'Rose', 'age': 33}
f'My wife name is {wife.get("name")}'
# 'My wife name is Rose'
f'She is {wife.get("age")} years old.'
# 'She is 33 years old.'
f'She is deeply in love with {wife.get("husband")}'
# 'She is deeply in love with None'

wife = {'name': 'Rose', 'age': 33}

f'She is deeply in love with {wife.get("husband", "lover")}'
# 'She is deeply in love with lover'




# Adding items with setdefault()
wife = {'name': 'Rose', 'age': 33}
if 'has_hair' not in wife:
    wife['has_hair'] = True
# Using the setdefault method we can make the same code more short:
wife = {'name': 'Rose', 'age': 33}
wife.setdefault('has_hair', True)
wife
# {'name': 'Rose', 'age': 33, 'has_hair': True}




# Removing Items
# pop()
# The pop() method removes and return an item based on a given key.
wife = {'name': 'Rose', 'age': 33, 'hair': 'brown'}
wife.pop('age')
# 33
wife
# {'name': 'Rose', 'hair': 'brown'}

# popitem()
# The popitem() method remove the last item in a dictionary and returns it.
wife = {'name': 'Rose', 'age': 33, 'hair': 'brown'}
wife.popitem()
# ('hair', 'brown')
wife
# {'name': 'Rose', 'age': 33}

# del()
# The del() method removes an item based on a given key.
wife = {'name': 'Rose', 'age': 33, 'hair': 'brown'}
del wife['age']
wife
# {'name': 'Rose', 'hair': 'brown'}

# clear()
wife = {'name': 'Rose', 'age': 33, 'hair': 'brown'}
wife.clear()
wife
# {}




# Checking keys in a Dictionary
person = {'name': 'Rose', 'age': 33}
'name' in person.keys()
# True
'height' in person.keys()
# False
'skin' in person # You can omit keys()
# False




# Checking values in a Dictionary
person = {'name': 'Rose', 'age': 33}
'Rose' in person.values()
# True
33 in person.values()
# True



# Pretty Printing
import pprint
wife = {'name': 'Rose', 'age': 33, 'has_hair': True, 'hair_color': 'brown', 'height': 1.6, 'eye_color': 'brown'}
pprint.pprint(wife)
# {'age': 33,
#  'eye_color': 'brown',
#  'hair_color': 'brown',
#  'has_hair': True,
#  'height': 1.6,
#  'name': 'Rose'}




# Merge two dictionaries
dict_a = {'a': 1, 'b': 2}
dict_b = {'b': 3, 'c': 4}
dict_c = {**dict_a, **dict_b}
dict_c
# {'a': 1, 'b': 3, 'c': 4}




# Initializing a set
# There are two ways to create sets: using curly braces {} and the built-in function set()
# Empty Sets When creating set, be sure to not use empty curly braces {} or you will get an empty dictionary instead.
s = {1, 2, 3}
s = set([1, 2, 3])
s = {}  # this will create a dictionary instead of a set
type(s)
# <class 'dict'>




# Unordered collections of unique elements
# A set automatically remove all the duplicate values.
s = {1, 2, 3, 2, 3, 4}
s
# {1, 2, 3, 4}

# And as an unordered data type, they can't be indexed.
s = {1, 2, 3}
s[0]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'set' object does not support indexing
=======
# Unordered collections of unique elements
>>>>>>> feature
















# Angela Notes
# Extend function is the same as +=
# Extend list by appending elements from the iterable
# Append vs extend does the same thing
# extend adds multiple elements list.extend((4,5))
# append adds 1 element list.append(1)