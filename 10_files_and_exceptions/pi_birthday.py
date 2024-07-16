with open('pi_digits.txt') as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.rstrip()

# print(len(pi_string))

birthday = input("Enter your birthday, in the form 'ddmmyyyy': ")
if birthday in pi_string:
	print("YES! Your birthday appears in the first million digits of pi!")
else:
	print("No... Your birthday does not appear in the first million digits of pi.")