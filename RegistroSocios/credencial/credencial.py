from PyPDF2 import PdfFileWriter, PdfFileReader
from io import BytesIO
from reportlab.pdfgen import canvas 
from reportlab.lib.pagesizes import letter 

packet = BytesIO() 
# create a new pdf with Reportlab
can = canvas.Canvas(packet, pagesize=letter) 
can.drawString(10, 100, "Hello world") 
can.save() 
#move to the beginning of the StringIO buffer 
packet.seek(0) 
new_pdf = PdfFileReader(packet) 
# read your existing PDF
existing_pdf = PdfFileReader(open("statics\img\original.pdf", "rb")) 
output = PdfFileWriter() 
# add the "watermark" (which is the new pdf) on the existing page 
page = existing_pdf.getPage(0) 
page.mergePage(new_pdf.getPage(0)) 
output.addPage(page) 
# finally, write "output" to a real file 

outputStream = open("destination.pdf", "wb") 
output.write(outputStream) 
outputStream.close()


