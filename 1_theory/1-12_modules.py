#1-12 Modules 
# modules = 기능의 집합
# module = java의 함수 같은 것 ,java 처럼 import 해줘야함
# library에서 import해서 사용 가능한 다양한 module을 확인할 수 있음 
#import math
#print(math.fsum(-1.2))  fabs : 절대값 
	#이런 식으로 import하면 모든 math module을 가져와서 비효율적임

from math import ceil,fsum
#from math import fsum as cute_sum
	# as를 통해 import해 온 module의 이름을 변경할 수 있음
#csv : common separated value

print(ceil(1.2))
print(fsum([1,2,3,4,5]))
#from을 통해서 특정 module만 가지고 오면 math.sth가 아니라
#sth으로만 사용 가능 .

from calculator import plus as deohagi,minus 
#다른 file에 있는 함수도 이런식으로 import 가능
# 이런식으로 import해온 함수 중 특정 함수만 as로 변경 가능 

print(deohagi(2,3),",",minus(1,2))