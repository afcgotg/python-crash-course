# 4-3. Counting to Twenty

for i in range(1, 21):
    print(i)

# 4-4 One Million

million = [i for i in range(1, 1_000_001)]
# for value in million:
#    print(value)

# 4-5 Summing a Million
print(min(million))
print(max(million))
print(sum(million))

# 4-6 Odd Numbers

odd = list(range(1, 20, 2))
for num in odd:
    print(num)

# 4-7 Threes

threes = list(range(3, 31, 3))
# threes = [3 * i for i in range(1,11)]
for num in threes:
    print(num)

# 4-8 Cubes

cubes = []
for i in range(1, 11):
    cubes.append(i**3)

for cube in cubes:
    print(cube)

# 4-9 Cube Comprehesion
cubes = [ i ** 3 for i in range(1,11)]
for cube in cubes:
    print(cube)
