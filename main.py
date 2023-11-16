import os
import wikipedia

files_names = []
pres_names = set()
pres_first_names = {}

if os.path.isdir("./cleaned") == False:
    os.mkdir("./cleaned")

def list_of_files(directory, extension): #Get all the name of files in the given directory with a specific extension
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

for i in list_of_files("./speeches","txt"): #Get all the presiden names from the speeches files in the speeches directory
    if i.endswith("0.txt") or i.endswith("1.txt") or i.endswith("2.txt") or i.endswith("3.txt") or i.endswith("4.txt") or i.endswith("5.txt") or i.endswith("6.txt") or i.endswith("7.txt") or i.endswith("8.txt") or i.endswith("9.txt"):
        pres_names.add(i[:-5].split("_")[-1])
    elif i[:-4].split("_")[-1]:
        pres_names.add(i[:-4].split("_")[-1])
    
    #Convert the speeches in lowercase stored in the directory ./cleaned
    with open(f"./speeches/{i}", 'r') as f1:
        with open(f"./cleaned/{i}",'a') as f2:
            for i in f1.read():
                if ord(i)>=65 and ord(i)<= 90:
                    f2.write(chr(ord(i)+32))
                else:
                    f2.write(i)

for i in pres_names: #Create a dictionnary that associates a first name to each president name
    pres_first_names[i] = wikipedia.search(i)[0].split(" ")[0]
print(pres_first_names)
