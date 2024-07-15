# 9-6 Ice Cream Stand

from second import Restaurant
from second import User

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type, flavours):
		super().__init__(restaurant_name, cuisine_type)
		self.flavours = flavours

	def show_flavours(self):
		for flavour in self.flavours:
			print(flavour)

ice_cream_stand = IceCreamStand("Cream ice", "italian", ["strawberry", "lemon",
 "vanilla", "chocolate"])
ice_cream_stand.show_flavours()


# 9-7 Admin

class Admin(User):
	def __init__(self, first_name, last_name, age, privilages):
		super().__init__(first_name, last_name, age)
		self.privilages = privilages

	def show_privilages(self):
		for privilage in self.privilages:
			print(privilage)

admin = Admin('Alex', 'Fernandez', 31, ['read all', 'edit all'])
admin.show_privilages()


# 9-8 Privilages

class Privilages:
	def __init__(self, privilages):
		self.privilages = privilages

	def show_privilages(self):
		for privilage in self.privilages:
			print(privilage)

class Admin(User):
	def __init__(self, first_name, last_name, age, privilages):
		super().__init__(first_name, last_name, age)
		self.privilages = privilages


privilages = Privilages(['read all', 'edit all'])
admin = Admin('Alex', 'Fernandez', 31, privilages)
admin.privilages.show_privilages()