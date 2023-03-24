import random

# a = [
# 	('Ruslan', 2004),
# 	('Kiril', 1955),
# 	('Lavrov', 1999),
# 	('Musi', 2004),
# 	('Erlan', 2003),
# 	('Beka', 2006),
# 	('Den', 1999),
# 	('Tilo', 1980),
# ]
#
# b = [block[0] for block in a if block[1] > 2000]
# print(b)

n = 7
m = 7

a = [
	[random.randint(1, 6) for j in range(m)]
	for i in range(n)
]

for item in a:
	print(item)