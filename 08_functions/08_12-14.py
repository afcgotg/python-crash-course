# 8-12 Sandwiches

def sandwich_ingredients(*ingredients):
	print("The sandwich will contain:")
	for ingredient in ingredients:
		print(f" -{ingredient.title()}")

sandwich_ingredients('cheese', 'tomatoe', 'meat')
sandwich_ingredients('cheese', 'meat')
sandwich_ingredients('meat')

# 8-13 User Profile

def build_profile(first_name, last_name, **kwargs):
	kwargs['first_name'] = first_name
	kwargs['last_name'] = last_name
	return kwargs

profile = build_profile('alex', 'fernandez', age=31, location='Terrassa')
print(profile)

# 8-14 Cars

# ...

