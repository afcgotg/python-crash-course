# 6-1 Person

person = {
        'first_name': 'john',
        'last_name': 'doe',
        'age': 42,
        'city': 'bern'
        }

for key, value in person.items():
    print(f"The '{key}' value is {value}")

# 6-2 Favorite Numbers

favorite_numbers = {
        'alex': 7,
        'nadine': 8,
        'manday': 13,
        'marc': 13,
        'uri': 3
        }

for key, value in favorite_numbers.items():
    print(f"The favorite number of {key.title()} is {value}")