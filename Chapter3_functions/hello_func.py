def hello():
    print('Howdy!')

def hello2(name):
    print(f'Hello {name}')

def choose(choice):

    if choice == 1:
        return hello()
    else:
        return print('Hello inside choose')

choose(2)

