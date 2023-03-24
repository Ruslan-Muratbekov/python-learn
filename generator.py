a = [i for i in range(3)]

def x():
  num = 7
  for i in a:
    yield i
    print(num)
    num = num * 10 + 7

num = x()

print(a)
print(next(num))
print(next(num))
print(next(num))