#1-7 Keyworded Arguments
def plus(a, b):
  return a - b

result = plus(2, 4)
  #위치로 인자를 확인하는 positional argument

k_result = plus(b=10,a=15)
print("result=",result,", k_result = ",k_result)
  # keyword argument는 argument의 이름으로 쌍을 이뤄줌

def introduction(name,age):
  return f"Hello I'm {name}, {age} years old"

#string 안에 인자 값을 넣어주기 위해서 string 앞에 format을 뜻하는 f를 적어준 뒤, string안에 인자가 들어갈 자리에 {인자이름} 기입

hi_every1 = introduction("moon","31")
print(hi_every1)

def introduce(name,age,are_from,fav_song):
  return f"Hello I'm {name}, {age} years old, I'm from {are_from}, and I love {fav_song}"

#이렇게 인자 값을 많을 때, keyword argument를 사용하는게 유용

hey = introduce( age="30", are_from="seoul", fav_song="george's boat", name="moonzero")
print(hey)
