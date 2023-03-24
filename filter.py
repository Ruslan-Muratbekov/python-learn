a = [x for x in range(100)]

res = list(filter(lambda x: x > 10 and x % 2 == 0 and x % 3 == 0, a))
print(res)