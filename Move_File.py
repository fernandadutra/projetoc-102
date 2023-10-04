import os
import shutil

from_dir = "C:/Users/55319/Documents/Code/ProjetoC-102"
to_dir ="C:/Users/55319/Documents/Code/ProjetoC-102/Arquivos_Documentos"

list_of_files= os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    print(name)
    print(extension)

    if(extension==""):
        continue
    if(extension in [".txt", ".doc", ".docx", ".pdf"]):
        #caminho de origem do arquivo
        path1= from_dir + "/" + file_name
        #caminho da pasta nova
        path2= to_dir
        #caminho do arquivo já na pasta nova
        path3= to_dir + "/" + "Arquivo_Documentos"

        if(os.path.exists(path2)):
            print("Movendo")
            #movendo o arquivo do path1 para o path 3
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)    
            print("Movendo")
            #movendo o arquivo do path1 para o path 3
            shutil.move(path1,path3)  