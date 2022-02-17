#1-11 for in
#python에서 정의하는 for in
	#string, tuple 또는 list 같이 배열의 요소를 순차적으로 가리킨다
days = ("Mon", "Tue", "Wed", "Thu", "Fri")

for day in days:
	if day == "Wed":
		break
	else:
		print(day)

for x in [1, 2, 3, 4, 5]:
	print(x)
#string도 하나의 배열
for letter in "moonyeong":
	print(letter)

# day, x 와 같은 for문 안의 변수가 만들어지는건 for문이 실행되는 순간

#nico 따라서 if day is "Wed":로 작성했더니 is에서 밑줄 뜨고 
#run했을 때 "Did you mean "=="? if day is "Wed":" 문장 뜸