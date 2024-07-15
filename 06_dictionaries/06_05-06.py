# 6-5 Rivers

rivers = {
        'nile': 'egypt',
        'amazon': 'brasil',
        'sena': 'france',
        'ebro': 'spain',
        'llobregat': 'spain'
        }

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)

# 6-6 Polling (alternative)

favorite_languages = {
        'maria': 'python',
        'alex': 'c++',
        'federico': 'rust',
        'susana': 'java',
        'bernardo': 'c++',
        'ana maria': 'ruby',
        'nadine': 'python',
        'manday': 'javascript',
        'guillem': 'python',
        'pau': 'c++',
        'josep': 'c++',
        'ivan': 'java'
        }

print(f"This list contains {len(set(favorite_languages.values()))} " +
        "different languages:")
for lenguage in sorted(set(favorite_languages.values())):
    print(lenguage)



