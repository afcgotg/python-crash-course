# 7-8 Deli

sandwich_orders = ['american', 'bacon', 'bagel toast', 'baked bean', 'barbacue', 'tuna']
finished_sandwiches = []

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print(f"I will make you {sandwich.title()} sandwich.")
	finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
	print(f"{sandwich.title()} has been made.")

# 7-9 No Pastrami

sandwich_orders = ['american', 'pastrami', 'bacon', 'pastrami', 'pastrami', 'bagel toast', 'baked bean', 'pastrami', 'barbacue', 'tuna', 'pastrami']
print("We run out of pastrami!")

print(sandwich_orders)
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
print(sandwich_orders)

# 7-10 Dream Vacation

dream_vacations = {}
active = True
while active:
	name = input("\nName :")
	destination = input("Destination: ")
	dream_vacations[name] = destination

	while True:
		response = input("There is someone else that want to answer the poll? (y/n)")
		if response == 'n':
			active = False
			break
		elif response == 'y':
			break
		else:
			print("Please, enter a valid answer (y/n):")