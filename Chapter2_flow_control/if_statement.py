from tkinter import X


var1 = int(input('Type an integer number:'))

var2 = int(input('Type an integer number:'))

if var1 > var2:
    print(f'var1 is greater than var2. var1 = {var1}, var2 = {var2}')
elif var1 < var2:
    print(f'var1 is less than var2. var1 = {var1}, var2 = {var2}')
else:
    print(f'var1 is equals to var2. var1 = {var1}, var2 = {var2}')
    #print('var1 is equals to var2. var1 = {}, var2 = {}'.format(var1,var2))
