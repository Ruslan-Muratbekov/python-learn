file = open('./test.txt', 'r', encoding='utf-8')
# file.write('Привет')
print(file.read())

# a - добавляем новое значение без стирание старых значении
# r - просто читает
# w - добавление новых значении и удаление старых значении