

def input_validation():
    while True:
        try:
            input_number = int(input('Type an integer number to collatz function:'))
            break
        except ValueError:
            print('Error value, type an valid integer next time!')
            
    return input_number


def check_even_number(number_to_check):
    if (number_to_check % 2) == 0:
        return True
    else:
        return False


def collatz(number, even_odd):
    if even_odd == True:
        return number // 2
    else:
        return 3*number+1        


result = 0

while result != 1:

    number = input_validation()
    result = collatz(number, check_even_number(number_to_check=number))
    print(result)



