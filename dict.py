d = {}
d['a'] = 1
print(d)
if 'a' in d:
	d['a'] += 1
else:
	d['a'] = 1

if 'a' in d:
	d['a'] += 1
else:
	d['a'] = 1

print(d)