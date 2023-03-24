r = lambda x: x ** 2
per = lambda a, b, c: a + b + c

print(r(7))
print(per(1, 1, 1))

a = [78, 234, 234, 234234, 5435, 567, 58879, 789, 90, 89, 5000]
a.sort(key=lambda x: x % 10)
print(a)


def linear(k, b):
	return lambda x: x * k + b


graf = linear(4, 5)
print(graf(3))
