class Car():
	wheels = 4
	doors = 4
	windows = 4
	seats = 4


	def start(self):
		print(self.doors)
		print("I started")

#method : function in class

zero = Car()
zero.start()
#모든 method의 첫번째 arguments는 그 method를 호출한 instance
#zero.start(zero)