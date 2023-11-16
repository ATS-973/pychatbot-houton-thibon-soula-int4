import os

files_names = []
pres_names = []

def list_of_files(directory, extension):
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

for i in list_of_files("./speeches","txt"):
    if i.endswith("0.txt") or i.endswith("1.txt") or i.endswith("2.txt") or i.endswith("3.txt") or i.endswith("4.txt") or i.endswith("5.txt") or i.endswith("6.txt") or i.endswith("7.txt") or i.endswith("8.txt") or i.endswith("9.txt"):
        if i[:-5].split("_")[-1] not in pres_names:
            pres_names.append(i[:-5].split("_")[-1])
            #print(i[:-5].split("_")[-1])
    elif i[:-4].split("_")[-1] not in pres_names:
        pres_names.append(i[:-4].split("_")[-1])
print(pres_names)