#pdf_extract
#Author: Brent Lang
#Date: 11/30/20
#Purpose: Program asks for filename to be processed from the user and extract pages from the file.  
#         Program will ask for the file names for input and output and then starting and ending pages to extract.

import PyPDF2 as pdf

input_file = input('Please enter a filename: ')
first_page = int(input('Please enter the beginning page number to extract: '))
last_page = int(input('Please enter the ending page number to extract: '))

while True:
#Page range validity check to see if last page is out of range for the PDF specified
    with open(input_file, 'rb') as pdf_range:
            page_check = pdf.PdfFileReader(pdf_range)
            if last_page > page_check.numPages:
                print('Your ending index is out of range, please enter correct ending page.')
                first_page = int(input('Please enter the beginning page number to extract: '))
                last_page = int(input('Please enter the ending page number to extract: '))
            
#Page number validity check to see if first and last pages are sequentially in order
            elif last_page < first_page:
                print('Your beginning and ending page numbers are not correct.')
                first_page = int(input('Please enter the beginning page number to extract: '))
                last_page = int(input('Please enter the ending page number to extract: '))
            else: break
            
output_file = input('Please enter output file name: ')

#Main body of program writes a new PDF using validated inputs specified by user
input_pdf = pdf.PdfFileReader(input_file)
page_range = []

for page in range((first_page - 1), ((last_page - 1 ) + 1 )):
    page_range.append(page)

pdfWriter = pdf.PdfFileWriter()
 
for page in page_range:
    pdfWriter.addPage(input_pdf.getPage(page))
 
with open(output_file, 'wb') as out_pdf:
    pdfWriter.write(out_pdf)
    out_pdf.close()