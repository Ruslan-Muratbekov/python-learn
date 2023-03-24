text = "Hello my name is Ruslan"

print(text[:])
print(text[:2])
print(text[2:])
print(text[1::2])

print(text.upper())
print(text.lower())
print(text.count('s'))

# find возвращает -1 если она не смогла найти
print(text.find('s'))
# index возвращает ошибку если не смогла найти
print(text.index('s'))

print(text.replace('s', '&&&&&&'))
print(text.replace('s', '&&&&&&', 1))

# проверка на что все в переменной из текста
print(text.isalpha())

# проверка что все в переменной в цифрах и это помогает при приоброзовании цифр string в цифр number
print(text.isdigit())

print(text.ljust(len(text) + 3, '0'))
print(text.rjust(len(text) + 3, '0'))

print('    '.join(text.split()))

print(input('Ввод: ').upper().strip())
print(input('Ввод: ').upper().lstrip())
print(input('Ввод: ').upper().rstrip())

data = [
	['Руслан', 'Муратбеков', 234],
	['Руслан', 'Муратбеков', 234],
	['Руслан', 'Муратбеков', 234],
]

for name, surname, balance in data:
	print(f"""Привет меня зовут {name + ' ' + surname}. У меня на балансе {balance}""")