# a = 3
# b = "like this"
# c = True
# bolean : true/false는 첫글자 대문자로 
# print(a)
# python에서는 대부분 snake 표기법을 사용
a_string = "like this"
a_number = 3
a_float = 3.14
a_boolean = False
# None = nothing, only python has . 
a_none = None

print(type(a_boolean))

#1-1 Lists in Python

#list = sequence type 중의 하나 
#list , tuple 
days = ["Mon","Tue","Wed","Thu","Fri"]
print(days)
#python standard library에 올라온 문법 check
print("Mon" in days) # -> True
print("Man" in days) # -> False

print(days[3]) # -> Thu
# -> java처럼 0부터 count

print(len(days)) # -> length 의미
#list는 mutable sequence라서 append(), reverse(), clear()등으로 변경 가능
days.append("Sat") # 추가
days.reverse()
print(days)