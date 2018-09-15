"""
    pip install PyPDF2
"""
import PyPDF2

pdf_file = open('./secreto.pdf', 'rb')
import pdb; pdb.set_trace()

read_pdf = PyPDF2.PdfFileReader(pdf_file)