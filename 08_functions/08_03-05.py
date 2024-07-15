# 8-3 T-Shirt

def make_shirt(size, text):
	print(f"T-shirt of size {size.upper()} with the message: '{text}'")

make_shirt('M', 'Hello world!')
make_shirt(size='xxl', text='This is a big big wolrd!')

# 8-4 Larg Shirts

def make_shirt(size = 'L', text = 'I love Python'):
	print(f"T-shirt of size {size.upper()} with the message: '{text}'")

make_shirt()
make_shirt('M')
make_shirt(size='xxl', text='This is a big big wolrd!')

# 8-5 Cities

def describre_city(city, country = 'unknow coutry'):
	print(f"{city.title()} is in {country.title()}.")

describre_city('la la land')
describre_city('berlin', 'germany')
describre_city('paris', 'france')
