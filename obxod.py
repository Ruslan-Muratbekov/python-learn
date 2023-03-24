import os

path = 'C:\\Test'

print(os.listdir(path))

def obxodFile(path, level=1):
	print('Level=', level, 'Content:', os.listdir(path))
	for i in os.listdir(path):
		if os.path.isdir(path + '\\' + i):
			print('Спускаемся', path+'\\'+i)
			obxodFile(path + '\\' + i, level+1)
			print('Возращаемся в ' + path)

obxodFile(path)
