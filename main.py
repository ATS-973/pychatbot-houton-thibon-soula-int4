import os

files_names = []
pres_names = []

def list_of_files(directory, extension):
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

for i in list_of_files("./speeches","txt"):
    if i.endswith("0","1","2","3","4","5","6","7","8","9") and i[:-1] not in pres_names:
        pres_names.append(i)
    elif i not in pres_names:
        pres_names.append(i)