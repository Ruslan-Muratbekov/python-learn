a = {1, 2, 3, 4, 5, 4, 3, 2, 1}

a.add(5)
a.update([1, 2, 3, 4, 5])

# без ошибки
a.discard(4)
# с ошибкой
a.remove(4)
