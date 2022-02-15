#1-6 Retunrs
#return의 역할 : 함수의 결과를 return, 함수 종료

def p_plus(a, b):
  print(a + b)

#return으로 이미 함수가 종료 되었으므로 print()는 실행되지 X
def r_plus(a, b):
  return a + b
  print("This sentence won't be printed out.")

p_result = p_plus(2, 3)
r_result = r_plus(2, 4)

print("p_result =",p_result,"r_result =", r_result)

#p_plus 함수에서 아무것도 return하지 않아서 
#print(p_plus)가 None으로 출력됨
#program은 print를 신경쓰지 X, print로 나타낸 값을 쓸 수 X
# -> print(~~) = None