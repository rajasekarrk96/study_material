import PyPDF2

# Open the PDF file in read-binary mode
pdf_file = open('sample.pdf', 'rb')

# Create a PDF file reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Get the number of pages in the PDF
num_pages = len(pdf_reader.pages)

# Initialize an empty string to store the text
pdf_text = ""

# Loop through each page and extract the text
for page in pdf_reader.pages:
    pdf_text += page.extract_text()

# Close the PDF file
pdf_file.close()

# Print the extracted text
print(pdf_text)
