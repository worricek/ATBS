#04_11_except
try:
	list = [1, 2, 3, 4]
	print(list[3])
except IndexError:
	print('Oops')
