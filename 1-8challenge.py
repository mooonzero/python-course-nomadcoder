#plus ,minus, times, division, negation(-x), power, reminder%
#1-8 code challenge !

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def is_on_list(a,b):
	return a.__contains__(b)

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

def get_x(a,b):
	return a[b]

print("The fourth item in 'days' is:", get_x(days, 3))

def add_x(a,b):
	return a.append(b)

add_x(days, "Sat")
print(days)

def remove_x(a,b):
	return a.remove(b)	
remove_x(days, "Mon")
print(days)

#https://replit.com/@mooonzero/Day-Two-Blueprint#main.py
