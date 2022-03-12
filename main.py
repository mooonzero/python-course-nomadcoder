# def plus(a, b, *args, **kwargs):
# 	print(args)
# 	print(kwargs)
# 	return a + b
# #*args : for positional arguments
# #**kwargs : for keyword arguments 
# 	#keyword arguments : somethg = 'hey'처럼 keyword가 설정된것
# 	# kwargs는 dict형으로 출력? 생성? 됨

# plus(1,1,1,1,1,1,2,4,5,2,moon =True, zero = True, hungry = True, beer = True)

def plus(*args):
	result = 0
	for number in args:
		result += number
	print(result)

plus(1,1,1,1,1,1,2,4,5,2,5,4)
