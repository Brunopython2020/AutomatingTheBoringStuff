
def comma(arg):
    string = ''
    try:
        if len(arg) == 0:
            string = 'Lista Vazia'
        else:
            for i,item in enumerate(arg):
                if i == 0:
                    string += f'{str(item)},'
                elif  0 < i < len(arg) - 1:
                    string += f' {str(item)},'
                elif i == len(arg) - 1:
                    string += f' and {str(item)}'
    except Exception as e:
        string = f'Error: {e}'

        
    return string


print(comma(['a',2,'b','True', False]))
print(comma(1))
