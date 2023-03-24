from decorator import *

@block
def say(name, surname):
    print(name, surname)

say('Ruslan', 'Muratbekov')