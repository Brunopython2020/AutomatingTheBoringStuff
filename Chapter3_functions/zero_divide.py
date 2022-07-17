def spam(divide_by):
    try:
        return 42/divide_by
    except:
        return '#ERROR: Can not divide 42 by ZERO'

a = 1
while a < 5:

    denominator = int(input('Type an integer number:'))
    print(spam(denominator))

    a+=1