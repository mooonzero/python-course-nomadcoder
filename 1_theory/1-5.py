#1-5 Function Arguments
#function 에 input을 줄 수 있음 
def say_hello(who):
  print("hello", who)

say_hello("Moonyeong")

def plus(a, b):
  print(a + b)

#b=0 -> b값이 없다면 0을 줘라  ->default value
def minus(a, b=0):
  print(a - b)

plus(2, 5)
minus(2)
minus(2,1)

def say_hi(name="anonymous"):
  print("hi! ,",name)

say_hi()
say_hi("moon")