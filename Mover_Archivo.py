import os 
import shutil

from_dir = "C:/Users/andbv/Downloads/Proyecto102/Descargas"
to_dir = "C:/Users/andbv/Downloads/Proyecto102/Archivos_Documentos"

list_of_files =os.listdir(from_dir)
print(list_of_files)


for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    
    if extension == '':
        continue
    
    if extension in [".txt", ".doc", ".docx",".pdf"]:
        ruta1 = from_dir + '/' + file_name
        ruta2 = to_dir + '/' + "Archivos_Documentos"
        ruta3 = ruta2 + '/' + file_name
        
        if os.path.exists(ruta2):
            print("Moviendo " + file_name + ".......")
            shutil.move(ruta1, ruta3)
        else:
            os.makedirs(ruta2)
            print("Moviendo" + file_name + ".......")
            shutil.move(ruta1, ruta3)