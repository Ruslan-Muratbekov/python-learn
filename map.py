def upperCase(x):
    return str(x).upper()

my_list = ['Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello']

res = list(map(upperCase, my_list))
print(res)