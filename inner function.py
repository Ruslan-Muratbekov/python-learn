g = 'Hello'

def colors():
    
    redColor = 'red'
    yellowColor = 'yellow'

    def red():
        nonlocal redColor
        print('red')

        return redColor
    
    def yellow():
        nonlocal yellowColor
        print('yellow')

        return yellowColor
    
    if red() == 'red':
        print(red())
        
colors()
    