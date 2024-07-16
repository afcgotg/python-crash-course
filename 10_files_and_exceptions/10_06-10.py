# 10-6 Addition

try:
	num_1 = int(input("Number 1: "))
	num_2 = int(input("Number 2: "))
except ValueError:
	print("Only numbers are accepted.")
else:
	print(f"{num_1} + {num_2} = {num_1 + num_2}")

# 10-7 Addition Calculator

while True:
		num_1 = input("Number 1: ")
		if num_1 == 'q':
			break
		num_2 = input("Number 2: ")
		if num_2 == 'q':
			break
		try:
			num_1 = int(num_1)
			num_2 = int(num_2)
		except ValueError:
			print("Only numbers are accepted.")
		else:
			print(f"{num_1} + {num_2} = {num_1 + num_2}")

# 10-8 Cats and Dogs
# 10-9 Silent Cats and Dogs

# 10-10 Common Words

file_name = "sherlock.txt"
try:
	with open(file_name) as f:
		content = f.read()
except FileNotFound:
	print("The file {file_name} doesn't exist.")
else:
	print(content.lower().count('the'))
	print(content.lower().count('the '))
	sentences = content.split('.')
	for sentence in sentences:
		print(sentence)

	print(len(set(content.lower().split())))
