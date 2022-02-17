#1.10 if else and or
def age_check(age):
	print(f"you're {age}")
	if age < 18 : 
		print("you can't drink")
	elif age == 18 or age == 19:
		print("you're new to this!")
	elif age > 20 and age < 25:
		print("you're still kind of young")
	else:
		print("enjoy your drink")	


age_check(29)

#elif = else if