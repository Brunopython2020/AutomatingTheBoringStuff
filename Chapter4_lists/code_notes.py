import random, copy


animals = ['cat', 'bat', 'rat', 'elephant']
numbers = [4,2,1,3]
cat = ['fat','gray','loud']
alfabet = ['a','C','A','b','Z','d','D','c']
name = 'BrunoGoncalvesSoares'

# Negative Indexes
"""
print(animals[-1]) #refers to the last index

print(animals[-2]) #basically the negative index access
"""


#Getting a List from Another List with Slices
"""print(animals[1:3])
print(animals[:3])
print(animals[:-1])"""

#List Concatenation and List Replication
"""
concatenated_list = animals + numbers
print(concatenated_list)
print(type(concatenated_list[-1]), type(concatenated_list[0])) #we can store differents data types in a list
"""

#Removing Values from Lists with del Statements
"""
del animals[1]

print(animals)
"""

#The in and not in Operators
"""
print('cat' in animals)
print('cat' not in animals)
"""

#The Multiple Assignment Trick
"""
##instead of doing this
###size = cat[0]
###color = cat[1]
###disposition = cat[2]

##Do this

size, color, disposition = cat

print(size,color,disposition)"""

#Using the enumerate() Function with Lists
"""
for index, item in enumerate(animals):
    print(str(index) + ' - ' + item)
"""

#Using the random.choice() and random.shuffle() Functions with Lists
"""
print(random.choices(animals)[0])
print(animals)
print(random.shuffle(animals))
print(animals)"""

#Finding a Value in a List with the index() Method
"""
print(animals.index('bat')) #When there are duplicates of the value in the list, the index of its first appearance is returned.

"""

#Adding Values to Lists with the append() and insert() Methods
"""
animals.append('Horse')
animals.insert(0,'Chicken')
print(animals)"""

#Removing Values from Lists with the remove() Method
"""
print(animals)
animals.remove('cat') #If the value appears multiple times in the list, only the first instance of the value will be removed.
print(animals)"""

#Sorting the Values in a List with the sort() Method
"""
print(numbers)
numbers.sort()
print(numbers)

print(animals)
animals.sort()
print(animals)

print(numbers)
numbers.sort(reverse=True)
print(numbers)

print(alfabet)
alfabet.sort()
print(alfabet)

alfabet.sort(key=str.lower) # If you need to sort the values in regular alphabetical order, pass str.lower for the key keyword argument in the sort() method call.
print(alfabet)"""

#Reversing the Values in a List with the reverse() Method
"""
print(animals)
animals.reverse()
print(animals)"""

#Sequence Data Types
"""
print(name[0:5])
print(name[-5:-1]) #strings are immutable

"""

#Converting Types with the list() and tuple() Functions
"""
a_tuple = tuple(animals)
print(a_tuple, type(a_tuple))

a_list = list(a_tuple)
print(a_list, type(a_list))

name = 'Bruno'
print(name, type(name))

print(list(name), type(list(name)))"""

#references
"""
spam = [0, 1, 2, 3, 4]

cheese = spam

print(cheese)

spam[0] = 'ZERO'

print(cheese)
"""

#Identity and the id() Function
"""
##The id() function identifies the python values in the computer memory
id_animals = id(animals)

print('animals: ', id_animals)

animals_copy = animals
id_animals_copy = id(animals_copy)

print('animals_copy: ', id_animals_copy)

tuple_test = (1,3,5,6,8)
tuple_test_copy = tuple_test

print('id_tuple_test: ',id(tuple_test))
print('id_tuple_test_copy: ',id(tuple_test_copy))"""

#The copy Module’s copy() and deepcopy() Functions

##Sometimes we do not want the parameters we pass to a function, point to the same id and therefore change the values of a mutable item outside the function
"""
spam = ['A', 'B', 'C', 'D']

print('id spam:', id(spam))

cheese = copy.copy(spam)

print('id cheese:', id(cheese))

spam.append(['a', 'b', 'c', 'd'])
spam.append([1, 2, 3, 4, 5])

cheese_burger = copy.deepcopy(spam)
print('id spam:', id(spam))
print('id cheese_burger: ', id(cheese_burger), 'cheese_burger: ', cheese_burger)"""



