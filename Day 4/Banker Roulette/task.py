import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

length_of_list = len(friends)

min = 0
max = length_of_list - 1

rand = random.randint(min, max)

print(friends[rand])
print(random.choice(friends))