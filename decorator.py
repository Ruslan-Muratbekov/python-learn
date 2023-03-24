from functools import wraps

def block(func):

	@wraps(func)
	def inner(*args, **kwargs):
		print('<div>')
		func(*args, **kwargs)
		print('</div>')
	
	return inner

def header (func):
    
		@wraps(func)
		def inner(*args, **kwargs):
			print('<table>')
			func(*args, **kwargs)
			print('</table>')
		
		return inner

@block
@header
def say(name, surname):
	print(name, surname)