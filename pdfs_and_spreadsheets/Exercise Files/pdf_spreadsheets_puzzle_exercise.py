# Task One: Grab the Google Drive Link from .csv File
import PyPDF2, re, csv

data = open('find_the_link.csv', encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)

link = []

i = 0

while i < len(data_lines):
    link.append(data_lines[i][i])
    i += 1

print(''.join(link))


# Task Two: Download the PDF from the Google Drive link and
# find the phone number that is in the document.

f = open('Find_the_Phone_Number.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(f)

for num in range(len(pdf_reader.pages)):

    page = pdf_reader.pages[num]
    page_text = page.extract_text()

    pattern = re.compile(r'(\d{3}).(\d{3}).(\d{4})')

    for match in re.finditer(pattern, page_text):
        print(match)

f.close()
