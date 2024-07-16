import json

# 10-11 Favorite Number

"""
number = input("What's your favorite number? ")

file_name = 'favorite_number.txt'
with open(file_name, 'w') as f:
	json.dump(number, f)

try:
	with open(file_name) as f:
		number = json.load(f)
except FileNotFoundError:
	pass
else:
	print(number)
"""


# 10-12 Favorite Number Remembered

def load_number():
	file_name = 'favorite_number.txt'
	try:
		with open(file_name) as f:
			number = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return number

def get_number():
	file_name = 'favorite_number.txt'
	number = input("What's your favorite number? ")
	with open(file_name, 'w') as f:
		json.dump(number, f)

number = load_number()
if number:
	print(f"Your favorite number is {number}")
else:
	get_number()


# 10-13 Verify User

def get_stored_username():
	filename = 'username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	username = input("What's your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f:
		json.dump(username, f)
	print(f"We'll remember you when you come back, {username}!")
	return username
		


def greet_user():
	username = get_stored_username()
	if username:
		print(f"The current user is {username}. Is this correct?")
		while True:
			answer = input("(y/n): ")
			if answer == 'y':
				print(f"Welcome back, {username}!")
				break
			elif answer == 'n':
				username = get_new_username()
				break
			else:
				answer = print("Invalid answer.")
	else:
		username = get_new_username()
		
greet_user()