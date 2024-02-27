import PyPDF2

f = open('Working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(f)
print(len(pdf_reader.pages))

page_one = pdf_reader.pages[0]
print(type(page_one))
page_one_text = page_one.extract_text()
print(page_one_text)

pdf_writer = PyPDF2.PdfWriter()
pdf_writer.add_page(page_one)

pdf_output = open('Some_Brand_New_Doc.pdf', 'wb')
pdf_writer.write(pdf_output)
pdf_output.close()

pdf_reader2 = PyPDF2.PdfReader(f)
pdf_text = []

for num in range(len(pdf_reader2.pages)):

    page = pdf_reader2.pages[num]

    pdf_text.append(page.extract_text())

print(pdf_text)

f.close()

