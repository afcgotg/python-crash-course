# 9-4 Number Served

class Restaurant:
	
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0


	def describe_restaurant(self):
		print(f"{self.restaurant_name} makes {self.cuisine_type} cuisine")

	def open_restaurant(self):
		self.open = True
		print(f"{self.restaurant_name} is opened")

	def set_number_served(self, num):
		self.number_served = num

	def increment_sumber_served(self, to_add):
		self.number_served += to_add

"""
restaurant = Restaurant("Taberna del ciri", "traditional")
print(restaurant.number_served)
restaurant.number_served = 3
print(restaurant.number_served)
restaurant.set_number_served(5)
print(restaurant.number_served)
restaurant.increment_sumber_served(15)
print(restaurant.number_served)
"""


# 9-5 Loggin Attempts

class User:
	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.loging_attempts = 0

	def describe_user(self):
		for key, value in self.__dict__.items():
			print(f"{key}: {value}")

	def greet_user(self):
		print(f"Hey {self.first_name.title()}!")

	def increment_login_attempts(self):
		self.loging_attempts += 1

	def reset_login_attempts(self):
		self.loging_attempts = 0

"""
user = User('Alex', 'Fernandez', 31)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.loging_attempts)
user.reset_login_attempts()
print(user.loging_attempts)
"""