# 7-1 Rental Car

car = input("What car do you want?\n  -")
print(f"Let me see if I can find you a {car}.")

# 7-2 Restaurant Seating

num_people = int(input("How many people are you?\n  -"))
if num_people > 8:
	print("You will have to wait for a table.")
else:
	print("Your table is ready.")

# 7-3 Multiples of Ten

num = int(input("Give me a number: "))
if num % 10 == 0:
	print("It's a multiple of ten!")
else:
	print("What a boring number...")