from collections import Counter, defaultdict, namedtuple

# COUNTER

mylist = [1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 8, 8, 8]

print(Counter(mylist))

newlist = ['a', 'a', 'a', 'a', 3, 3, 3, 3, 3, 3, 3]

print(Counter(newlist))

letters = 'aaaaaaaaaasssssssssssssssddddddddddddffffffffffffffggggggggggghhhhhhhhh'

print(Counter(letters))

c = Counter(letters)

print(c.most_common(2))

print(list(c))

sentence = "Susie works in a shoeshine shop. Where she shines she sits, and where she sits she shines."

print(Counter(sentence.split()))

# DEFAULT DICTIONARY

d = defaultdict(lambda : 0)

d['correct'] = 100
d['WRONG KEY!']

print(d['correct'])
print(d['WRONG KEY!'])
print(d)

# NAMEDTUPLE

Dog = namedtuple('Dog', ['age', 'breed', 'name'])
sammy = Dog(age=5, breed='Husky', name='Sam')

print(sammy.age)
print(sammy[1])


























