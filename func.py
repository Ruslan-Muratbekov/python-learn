# def f(a, b):
# 	print(id(a), id(b))
# 	a = 100
# 	b[0] = 10
# 	print(id(a), id(b))
#
# c = 20
# d = [1, 2, 3, 4]
# f(c, d)
# print(c, d, 'global')

# def f(a='Привет', b='Hello', c=4):
# 	print(a, b, c)
#
#
# f()
# f(a='Пока', b="Good Night", c='10')

# a = 10
# b = 11
#
# def f():
# 	global a
# 	a = 5
# 	b = 5
# 	print(a, b)
#
# f()
# print(a, b)

# def f(*args):
# 	print(list(a))
#
#
# f("Hello", 3, 4, 5, 5, 5, 7, 7)

# def f(*args, **kwargs):
# 	print(args, '*args')
# 	print(kwargs, '**kwargs')
# 	for k, v in kwargs.items():
# 		print(k, v)
#
#
# f(2, 3, 4, 5, 6, a=3, b=2, c='d')

# def outPrint(*args, sep='#', end='@'):
# 	print(args, sep, end)


# outPrint(1, 2, 3, 4, 5, sep='90', end=111)

# def f(a, b, c, d):
# 	print(a, b, c, d)
#
#
# a = [True, 1, 2, 3]
#
# f(*a)


def rec(x):
	print(x)
	if x > 200:
		return 20
	else:
		rec(x + 1)

print(rec(1))