my_cat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

"""print(my_cat['color'])
print(my_cat['disposition'])
print(my_cat['size'])"""

your_cat = {'color': 'gray', 'disposition': 'loud', 'size': 'fat'}


my_cat == your_cat # the order does not matter to compared if two dictionaries ares equals


# keys(), values() and items() methods
"""
spam = {'color': 'red', 'age': 42}

for v in spam.values():
    print(v)

for k in spam.keys():
    print(k)

for k,v in spam.items():
    print(f'k: {k}, v: {v}')

for i in spam.items():
    print(i)"""

#Checking Whether a Key or Value Exists in a Dictionary
"""
spam = {'name': 'Zophie', 'age': 7}
print('name' in spam.keys())
print('name' in spam.values())"""

#The get() Method
"""
picnicItems = {'apples': 5, 'cups': 2}

print('I am bringing ' + str(picnicItems.get('apples',0)) + ' eggs.')
"""
#The setdefault() Method
"""
spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'

print(spam)

spam.setdefault('height', 6.5) #The setdefault() method is a nice shortcut to ensure that a key exists.

print(spam)"""

#Pretty Printing
"""
Exemple in chacacter_count.py
"""

#Nested Dictionaries and Lists

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}


def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))