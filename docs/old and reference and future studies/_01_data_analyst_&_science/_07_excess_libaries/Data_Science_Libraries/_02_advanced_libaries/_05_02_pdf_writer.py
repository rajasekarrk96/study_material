#pipenv install fpdf

from fpdf import FPDF


# Create instance of FPDF class
pdf = FPDF()


# Add a page
pdf.add_page()

# Set font for the entire document
pdf.set_font("Arial", size = 12)

# Add a cell
pdf.cell(200, 10, txt = "Hello, this is a PDF generated using PyFPDF! hello raj", ln=True, align='C')

# Save the PDF to a file
pdf.output("output.pdf")
