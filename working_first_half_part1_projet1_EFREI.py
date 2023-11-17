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


def names(files_names):
    pres_names = set()
    str_name = ''
    for el in files_names:
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


def first_name_n_name():
    presidents = []
    for el in pres_names:
        presidents.append(president_Vrep[el]+" " + el)
    return presidents


presidents = first_name_n_name()


def display_pres_name_list():
    return print(presidents)


def convert_characters_f():
    new_filesnames = []
    for elt in files_names:
        new_file = elt[:-4]+"_update.txt"
        new_filesnames.append(new_file)
        with open("speeches/"+elt, 'r') as original_f, open(new_file, "a") as new_f:
            line = original_f.readline()
            while line != "":
                new_f.write(line.lower())
                line = original_f.readline()
    return new_filesnames


new_filesnames = convert_characters_f()
convert_characters_f()


