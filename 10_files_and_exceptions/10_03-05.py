# 10-3 Guest

name = input("What's your name? ")
with open('guest.txt', 'w') as file_object:
	file_object.write(name)

# 10-4 Guest Book

file_object = open('guest_book.txt', 'w')
file_object.close()
while True:
	name = input("What's your name? ")
	if name == 'quit':
		break
	print(f"Hi {name.title()}!")
	with open('guest_book.txt', 'a') as file_object:
		file_object.write(f"{name.title()}\n")

# 10-5 Programming Poll

file_object = open('programming_poll.txt', 'w')
file_object.close()
while True:
	reason = input("Why do you like programming? ")
	if reason == 'quit':
		break
	with open('programming_poll.txt', 'a') as file_object:
		file_object.write(f"{reason}\n")