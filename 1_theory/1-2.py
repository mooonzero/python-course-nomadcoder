# 1-2 tuples and dicts
tup_days = ("Mon","Tue","Wed","Thu","Fri")
print(type(tup_days)) # class tuples

# name = "moon"
# age = 32
# Korean = True
# fav_food = ["Coffee","Bab"]
# 이런식으로 변수를 설정하는 건 큰 도움 X 
#dictionary 설정하는 방법
moon = {
  "name" : "Moon",
  "age" : 31,
  "korean" : True,
  "fav_food" : ["Coffee","Bab"]
}
print(moon)
print(moon["fav_food"])
moon["starving"] = True
print(moon)
#어떤 변수든 list,tuple,dict 안에 설정 가능
anything = ("tada",True,7,None,False,"hey")
print(anything)