example_list = list(range(1,100, 7))

# 4-10 Slices

print("The first three items in the list are:")
for item in example_list[:3]:
    print(item)

x = 2
print("Three items from the middle of the list are:")
for item in example_list[x:(x+3)]:
    print(item)

print("The last three items in the list are:")
for value in example_list[-3:]:
    print(value)

# My Pizzas, Your Pizzas

pizzas = ["margarita", "carbonara", "pinnaple", "four cheeses"]
friend_pizzas = pizzas[:]

pizzas.append("pepperonni")
friend_pizzas.append("tuna")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My ifriend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
