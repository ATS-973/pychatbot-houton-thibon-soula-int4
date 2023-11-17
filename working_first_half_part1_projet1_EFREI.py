import os


def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


# Call of the function
directory = "./speeches"
files_names = list_of_files(directory, "txt")


# Function to get all president's names who have a speech file
def names(files_names):
# Use of a set to avoid repetitions
    pres_names = set()
# str_name is a string that will collect the name of the president written in the file name
    str_name = ''
    # Loop to go through all files names
    for el in files_names:
        # Loop to collect the name in the file
        for i in range(len(el)):
            if 49 <= ord(el[11+i]) <= 57 or el[11+i] == '.':
                pres_names.add(str_name)
                str_name = ''
                break
            else:
                str_name += el[11+i]
    return pres_names


pres_names = names(files_names)
president_Vrep = {"de Gaulle": "Charles", "Pompidou": "Georges", "Giscard dEstaing": "Valéry", "Mitterrand": "François", "Chirac": "Jacques", "Sarkozy": "Nicolas", "Hollande": "François", "Macron": "Emmanuel"}


# Function to associate president's name with his first name
def first_name_n_name():
    presidents = []
    for el in pres_names:
        presidents.append(president_Vrep[el]+" " + el)
    return presidents


presidents = first_name_n_name()


# Function to display the list of presidents
def display_pres_name_list():
    return print(presidents)


# Function to remove any Uppercase and punctuations
def convert_characters_f():
    for elt in files_names:
        new_file = "Cleaned/"+elt[:-4]+"_update.txt"
        with open("speeches/"+elt, 'r', encoding='utf-8') as original_f, open(new_file, "a", encoding='utf-8') as new_f:
            line = original_f.readline()
            while line != "":
                line = line.replace("'" or "-", " ")
                for i in range(33, 48):
                    line = line.replace(chr(i), "")
                for i in range(58, 65):
                    line = line.replace(chr(i), "")
                for i in range(91, 97):
                    line = line.replace(chr(i), "")
                for i in range(123, 127):
                    line = line.replace(chr(i), "")
                new_f.write(line.lower())
                line = original_f.readline()
    return

convert_characters_f()
