import math, random

num = 3.157

print(math.floor(num)) # Round down
print(math.ceil(num)) # Round up
print(math.pi)
print(math.log(8,2))
print(math.degrees(math.pi/2))
print("\n")


print(random.randint(0,100))
print("\n")

print("Seed demo starts here: ")
# This statement ensures that the same number is generated each time for each instance
random.seed(29)
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print("\n")

mylist = list(range(0,20))

print(random.choice(mylist))
# Allows random number to be chosen more than once
print(f"Sample with replacement: {random.choices(population=mylist, k=10)}")
# Random numbers chosen have to be unique
print(f"Sample without replacement: {random.sample(population=mylist, k=10)}")
# Every number has an equal chance to be chosen
print(random.uniform(a=0, b=100))

random.shuffle(mylist)
print(mylist)




