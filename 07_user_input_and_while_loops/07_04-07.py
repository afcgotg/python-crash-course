# 7-4 Pizza Toppings

while True:
	topping = input("Topping to add: ")
	if topping == 'quit':
		break;
	else:
		print(f"We will add {topping} to your pizza!")

# 7-5 Movie Tickets

while True:
	age = input("How old are you?\n  -")
	if age == 'quit':
		break;
	else:
		age = int(age)
		if age < 3:
			print("The ticket is free!")
		elif age <= 12:
			print("The ticket is 10$.")
		else:
			print("The ticket is 15$.")

# 7-6 Three Exits

active = True
while active:
	age = input("How old are you?\n  -")
	if age == 'quit':
		break;
	else:
		age = int(age)
		if age < 18:
			print("This is a porn movie! What the hell are you doing here?" +
				"\nwe are going to call the police right now!")
			active = False
		else:
			print("The ticket is 15$.")

# 7-7 Infinity

while True:
	print("Are you still there?")