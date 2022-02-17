def plus(a, b):
	if type(b) is int or type(b) is float:
		return a + b
	else: 
		return None

#str : string의 type을 나타냄
#is : object identity

print(plus(12, 1.2))