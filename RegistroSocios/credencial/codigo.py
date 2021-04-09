import qrcode 


imagen = qrcode.make('0914984521') 
archivo_imagen = open('codigo.jpg', 'wb')
imagen.save(archivo_imagen)
archivo_imagen.close()