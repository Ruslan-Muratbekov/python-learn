# import dir.generate2 as generate2
# print(generate2.say())
# generate2.floor()

# from dir.generate2 import my_str
# from generate2 import say, my_str
# print(say(), my_str)

# import dir.generate2 as generate2
# from importlib import reload
#
# print(generate2.my_str)
#
# generate2.my_str = "GOOD BAY!"
#
# print(generate2.my_str)
#
# import dir.generate2 as generate2
#
# print(generate2.my_str, "второй import")
#
# reload(generate2)
#
# print(generate2.my_str, "reload import")

import dir.generate2 as generate2

print(__name__)
print(generate2.__name__, "Мы можем узнать имя файла которую мы import")

if generate2.__name__ == "dir.generate2":
	print("dir.generate2 успешно импортирован")

# мы с помощью этого можем сделать так что бы определенные функции работали в конкретном файле