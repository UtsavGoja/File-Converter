# REMAINDER : Comment Out docx2pdf while performing pdf2docx and vice-versa

# FOR DOCX TO PDF FILES

from docx2pdf import convert

convert("File Converter/new.docx", "File Converter/new.pdf")



# FOR PDF TO DOCX FILES

from pdf2docx import Converter

obj = Converter("File Converter/new.pdf")
obj.convert("File Converter/new2.docx")
obj.close()