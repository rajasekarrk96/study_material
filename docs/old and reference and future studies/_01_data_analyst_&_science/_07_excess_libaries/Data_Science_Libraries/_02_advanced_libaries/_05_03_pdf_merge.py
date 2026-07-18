import PyPDF2


# Function to merge PDFs
def merge_pdfs(paths, output):
    pdf_writer = PyPDF2.PdfWriter()

    for path in paths:
        pdf_reader = PyPDF2.PdfReader(path)
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

    with open(output, 'wb') as out_pdf:
        pdf_writer.write(out_pdf)


# List of PDF files to merge
pdf_files = ['output.pdf', 'sample.pdf']

# Output file path
output_pdf = 'merged.pdf'

# Merge PDFs
merge_pdfs(pdf_files, output_pdf)
