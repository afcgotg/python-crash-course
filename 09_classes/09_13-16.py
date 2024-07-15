from random import randint, choice

# 9-13 Dice

class Dice:
	def __init__(self, sides):
		self.sides = sides

	def roll(self):
		return randint(1, self.sides)

d20 = Dice(20)
print(d20.roll())

# 9-14 Lottery

options = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E')
win_option = []
for i in range(1, 5):
	win_option.append(choice(options))

print(f"Any ticket machiching these: {win_option} wins a prize.")

# 9-15 Lterrery Analysis

options = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E')
my_ticket = ('A', 7, 3, 'E')
counter = 0

while True:
	counter += 1
	win_option = []
	for i in range(1, 5):
		win_option.append(choice(options))

	if win_option == list(my_ticket):
		break

print(f"I win the lottery at the {counter} try.")

