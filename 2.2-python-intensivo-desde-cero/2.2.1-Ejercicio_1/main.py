import os

ruta = 'E:\\Users\\your_user_here\\Downloads'
directorio = os.fsencode(ruta)

for archivo in os.listdir(directorio):
    nombreArchivo = os.fsdecode(archivo)
    print(os.path.join(ruta, nombreArchivo))

# Nota 1 - Imprimir archivos con determinada extensión
# if filename.endswith(".jpg") or filename.endswith(".png"):
#       print(os.path.join(ruta, nombreArchivo))
#       continue
# else:
#       continue

# Nota 2 - Mismo resultado con un único método
# directorio = os.listdir('E:\\Users\\Guido\\Downloads')
