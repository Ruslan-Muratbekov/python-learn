a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = ['value', 'value', 'value', 'value', 'value', 'value', 'value', 'value', 'value', 'value']

c = ['key', 'key', 'key', 'key', 'key', 'key', 'key', 'key', 'key', 'key']

res = list(zip(a, b, c))

for num, value, key in res:
    print(num, value, key)