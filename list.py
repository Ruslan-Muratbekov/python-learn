my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(my_list)

print(max(my_list))
print(min(my_list))
print(sum(my_list))
print(sorted(my_list))
print(sorted(my_list, reverse=True))

# findNumber = int(input('Ввод цифры которую хотите найти: '))

# if findNumber in my_list:
# 	print('success')
# else:
# 	print('false')

print(my_list[0])
print(my_list[5])
print(my_list[6])
print(my_list[-2])
print(my_list[:])
print(my_list[:2])
print(my_list[2:])
print(my_list[0:2])

# ::2 - первым параметро ':' мы берем все элменеты а вторым :2 мы указываем что бы по 2 брала
print(my_list[::2])

# 1::2 - 1: бы берем все элементы начиная с 1 до конца и :2 мы указываем каким шагом надо брать
print(my_list[1::2])

# 1:7:2 - 1:7 мы установили ограничение а в :2 мы указали шаги
print(my_list[1:7:2])

# берем с конца когда отрицательное число
print(my_list[::-2])

my_list.append({
	'title': 'title'
})

new_my_list = my_list.copy()
print(my_list)
print(my_list.clear(), 'очистка list')

print(new_my_list.count({'title': 'title'}), 'count')
print(new_my_list.index({'title': 'title'}), 'index')

new_my_list.insert(10, {'new': 'new'})
print(new_my_list, 'добавление {new: new} list')

print(new_my_list.pop())
new_my_list.remove({'new': 'new'})
print(new_my_list, 'удаление {new: new} list')

new_my_list.reverse()
print(new_my_list, 'reverse')

new_my_list.sort()
print(new_my_list, 'sort')

new_my_list.sort(reverse=True)
print(new_my_list, 'sort reverse')
print([0] * 10)