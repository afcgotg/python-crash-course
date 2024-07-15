# 6-7 People

person_1 = {
        'first_name': 'alex',
        'last_name': 'fernandez',
        'age': 31,
        'city': 'terrassa'
        }

person_2 = {
        'first_name': 'nadine',
        'last_name': 'soler',
        'age': 30,
        'city': 'terrassa'
        }

person_3 = {
        'first_name': 'gal·la',
        'last_name': 'soler',
        'age': 0,
        'city': 'terrassa'
        }

people = [person_1, person_2, person_3]

for person in people:
    for key, value in person.items():
        print(f"'{key}': '{value}'")
    print("\n")

# 6-8 Pets

pet_1 = {
        'name': 'neula',
        'kind': 'dog',
        'gender': 'female',
        'owner': 'alex'
        }

pet_2 = {
        'name': 'mylo',
        'kind': 'cat',
        'gender': 'male',
        'owner': 'alex'
        }

pets = [pet_1, pet_2]

for pet in pets:
    for key, value in pet.items():
        print(f"'{key}': '{value}'")
    print("\n")

# 6-9 Favorite Places

favorite_places = {
        'first_name': 'alex',
        'last_name': 'fernandez',
        'places': ['panama', 'vienn', 'lisbon']
        }

favorite_numbers = {
        'first_name': 'alex',
        'last_name': 'fernandez',
        'numbers': [7, 17, 3]
        }

cities = {
        'new_york': {
            'country': 'USA',
            'population': '3000000',
            'fact': 'nice hot dogs'
            },
        'barcelona': {
            'country': 'spain',
            'population': '1000000',
            'fact': 'tourist go home'
            },
        'paris': {
            'country': 'france',
            'population': '2500000',
            'fact': 'nice museums'
            }
        }
for city, infos in cities.items():
    print(f"From {city.title()} we know:")
    for info, value in infos.items():
        print(f"{info.title()}: {value.title()}")
    print("\n")

#                 ^
# 6-12 Extensions |



