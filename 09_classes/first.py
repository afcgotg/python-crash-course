# 9-1 Restaurant

class Restaurant:
	
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type


	def describe_restaurant(self):
		print(f"{self.restaurant_name} makes {self.cuisine_type} cuisine")

	def open_restaurant(self):
		self.open = True
		print(f"{self.restaurant_name} is opened")

restaurant = Restaurant("Taberna del ciri", "traditional")
restaurant.describe_restaurant()
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)


# 9-2 Three Restaurants

restaurant_1 = Restaurant("Taberna del ciri", "traditional")
restaurant_2 = Restaurant("Totoro", "japanes")
restaurant_3 = Restaurant("Juaner's", "american")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()


# 9-3 Users

class User:
	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age

	def describe_user(self):
		for key, value in self.__dict__.items():
			print(f"{key}: {value}")

	def greet_user(self):
		print(f"Hey {self.first_name.title()}!")

user_1 = User('Alex', 'Fernandez', 31)
user_1.greet_user()
user_1.describe_user()

user_2 = User('Gal·la', 'Soler', 0)
user_2.greet_user()
user_2.describe_user()