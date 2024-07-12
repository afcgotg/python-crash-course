# 3-4. Guest List

guests = ["shreck", "asno", "fiona", "gato"]

# 3-5. Changing guest list

print(guests[1].title())

# guests[1] = "pinoccio"

guests.remove('asno')
# del guests[1]
# guests.pop(1)

guests.insert(1, "pinoccio")

for guest in guests:
    print(f"Dear {guest.title()}, hope you can join us to the dinner")

# 3-6. More Guests

print("We found a bigger table!")
guests.insert(0, "king")
guests.insert(int(len(guests)/2), "queen")
guests.append("Lucas")

for guest in guests:
    print(f"Dear {guest.title()}, hope you can join us to the dinner")

# 3-7. Shrinking Guest List

print("Finally... I can only invite 2 guest for the dinner...")
while len(guests) > 2:
    guest = guests.pop()
    print(f"I'm so sorry {guest.title()}, but the table is too small...")


for guest in guests:
    print(f"Dear {guest.title()}, you're still invited to the dinner")

del guests[1]
del guests[0]

print(guests)

    
