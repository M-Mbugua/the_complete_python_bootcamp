import os, re, shutil

shutil.unpack_archive('unzip_me_for_instructions.zip', 'instructions', 'zip')

with open('instructions/extracted_content/Instructions.txt') as f:
    content = f.read()
    print(content)

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

def search(file, pattern = r'(\d{3})-(\d{3})-(\d{4})'):
    f = open(file, 'r')
    text = f.read()

    if re.search(pattern, text):
        return re.search(pattern, text)

    else:
        return ''

path = 'C:\\Users\\user\\Documents\\GitHub\\python\\instructions\\extracted_content'

results = []

for folder, sub_folders, files in os.walk(path):

    for f in files:
        full_path = folder+'\\'+f

        results.append(search(full_path))

for r in results:
    if r != '':
        print(r.group())



