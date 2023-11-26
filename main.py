import os
import tfIdf
import functions

files_names = []
pres_names = set()
pres_first_names = {'Giscard dEstaing':'Valérie', 'Macron':'Emmanuel', 'Mitterrand':'François', 'Sarkozy':'Nicolas', 'Hollande':'François', 'Chirac':'Jacques'}

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
    
    #Convert the speeches in lowercase, remove the punctuation and store them in the directory ./cleaned
    with open(f"./speeches/{i}", 'r', encoding='utf-8') as f1:
        with open(f"./cleaned/{i}",'w', encoding='utf-8') as f2:
            for i in f1.read():
                if ord(i) >= 48 and ord(i) <= 57 or ord(i)>=65 and ord(i)<= 90 or ord(i) >= 97 and ord(i) <= 122:
                    f2.write(i.lower())

                if not(ord(i) >= 48 and ord(i) <= 57 or ord(i) >= 65 and ord(i) <= 90 or ord(i) >= 97 and ord(i) <= 122):
                    if ord(i) > 127:
                        f2.write(i)
                    else:
                        f2.write(" ")

print(functions.unimportantWords("./cleaned"))