from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse

from RegistroSocios.models import Persona

def crear_pdf(request, pk):
    # Obtenemos un queryset, para un determinado libro usando pk.
    try:
        persona = Persona.objects.get(id=pk)
    except ValueError:
        raise Http404()
    # Creamos un objeto HttpResponse con las cabeceras del PDF correctas.
    response = HttpResponse(content_type='application/pdf')
    # Nos aseguramos que el navegador lo abra directamente.
    response['Content-Disposition'] = 'filename="archivo.pdf"'
    buffer = BytesIO()

    # Creamos el objeto PDF, usando el objeto BytesIO como si fuera un "archivo".
    p = canvas.Canvas(buffer)

    # Dibujamos cosas en el PDF. Aqui se genera el PDF.
    # Consulta la documentación de ReportLab para una lista completa de funcionalidades.
    p.drawString(100, 800, "Titulo: " + str(persona.nombre))
    p.drawString(100, 780, "Editor: " + str(persona.apellido))
    p.drawString(100, 760, "Portada " )
    #p.drawImage(str(libro.portada.url), 100, 150, width=400, height=600)

    # Cerramos limpiamente el objeto PDF.
    p.showPage()
    p.save()

    # Traemos  el valor de el bufer BytesIO y escribimos la respuesta.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response























'''from PyPDF2 import PdfFileWriter, PdfFileReader
from io import BytesIO
from reportlab.pdfgen import canvas 
from reportlab.lib.pagesizes import letter
from RegistroSocios.models import Persona, Categoria, Puesto

packet = BytesIO() 
# create a new pdf with Reportlab
can = canvas.Canvas(packet) #buffer
can.drawString(100, 800, 'casa')
can.drawString(100, 800, 'hoja')
can.drawString(100, 780, 'perro')
can.drawString(100, 760, "Portada ")
#can.drawImage(str(libro.portada.url), 100, 150, width=400, height=600)
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
outputStream.close()'''


