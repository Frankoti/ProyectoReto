import qrcode 

-
imagen = qrcode.make('0914984539') 
archivo_imagen = open('codigo.png', 'wb')
imagen.save(archivo_imagen)
archivo_imagen.close()