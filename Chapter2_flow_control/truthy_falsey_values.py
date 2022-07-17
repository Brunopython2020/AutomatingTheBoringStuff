"""
“TRUTHY” AND “FALSEY” VALUES

Conditions will consider some values in other data types equivalent to True and False.
When used in conditions, 0, 0.0, and '' (the empty string) are considered False,
while all other values are considered True. For example, look at the following program:

"""

name = ''
a = 1

while not name:
    print('While Lopp')
    a+=1
    if  a > 5:
        print(f'a = {a}')
        break



