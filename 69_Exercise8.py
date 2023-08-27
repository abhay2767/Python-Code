""" Write a program to manipulate pdf files using pyPdf. Your programs should be able to
    merge multiple pdf files into a single pdf. You are welcome to add more functionlaties.
    #:- pyPdf is a free and open-source pure-python PDF library capable of splitting, merging,
        cropping, and transforming the pages of PDF files. It can also add custom data, vewing
        option, and passwords to PDF "files.pypdf" can retrieve text and metadata from PDFs as well. 
 """
from PyPDF2 import PdfWriter
import os

merger = PdfWriter()

files = [file for file in os.listdir("clutteredPhotos") if file.endswith(".pdf")]
for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()