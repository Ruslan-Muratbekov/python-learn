import json5

# json = """{
# 	response: {
# 		name: 'Ruslan'
# 	}
# }"""
#
# data = json5.loads(json)
# # new_json = json5.dumps(data, indent=2)
#
# with open('my.json', 'w') as file:
# 	json5.dump(data, file, indent=2)

with open('my.json', 'r') as file:
	data = json5.load(file)
print(data)
print(type(data))

# load - нужен когда нам нужно прочитать ФАЙЛ JSON
# loads - нужен когда нам нужно прочитать СТРОКУ JSON

# dump - создает JSON ФАЙЛ
# dumps -создает СТРОКУ JSON