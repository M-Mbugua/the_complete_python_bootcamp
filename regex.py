import re

text = "The agent's phone number is 400-555-1234. Call now!"
pattern = 'phone'
match = re.search(pattern, text)

print(match)
print(match.span())
print(match.start())
print(match.end())

# search returns only the first instance of a match

text1 = "My phone once, my phone twice"
match1 = re.search(pattern, text1)

print(match1)

# findall returns all instances of a match but not the span

matches = re.findall(pattern, text1)

print(matches)
print(len(matches))

# iterating over the text; combination of search and findall

for match in re.finditer(pattern, text1):
    print(match.span())
    print(match.group())

# REGULAR EXPRESSIONS SYNTAX

text2 = "My number is 400-555-1234"
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text2)
phone1 = re.search(r'\d{3}-\d{3}-\d{4}', text2)
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern, text2)

print(phone)
print(phone.group())
print(phone1)
print(results.group(1))

# (.) is a wildcard character, it will return the character(s)
# based on how many are there
print(re.findall(r'.at', 'The cat in the hat sat there.'))
print(re.findall(r'...at', 'The cat in the hat sat there.'))

# Starts with (^)
print(re.findall(r'^\d', '1 is a number.'))

# Ends with ($)
print(re.findall(r'\d$', 'The number is 2.'))

# Exclusion
phrase = "There are 3 numbers 34 inside 5 this sentence."
pattern2 = r'[^\d]+'
print(re.findall(pattern2, phrase))

test_phrase = "This is a string! But it has punctuation. How can we remove it?"
clean = re.findall(r'[^!.? ]+', test_phrase)

print(clean)
print(' '.join(clean))


text3 = "Only find hyphenated-words. But you do not know how long-ish they are."
pattern3 = r'[\w]+-[\w]+'
print(re.findall(pattern3, text3))


# Brackets for multiple options

# Find words that start with cat and end with one of these options: 'fish','nap', or 'erpillar'
textone = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"

print(re.search(r'cat(fish|nap|erpillar)',textone))
print(re.search(r'cat(fish|nap|erpillar)',texttwo))
print(re.search(r'cat(fish|nap|erpillar)',textthree))