import math
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
def list_of_files(directory, extension):  # Get all the name of files in the given directory with a specific extension
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


for i in list_of_files("./speeches",
                       "txt"):  # Get all the presiden names from the speeches files in the speeches directory
    if i.endswith("0.txt") or i.endswith("1.txt") or i.endswith("2.txt") or i.endswith("3.txt") or i.endswith(
            "4.txt") or i.endswith("5.txt") or i.endswith("6.txt") or i.endswith("7.txt") or i.endswith(
            "8.txt") or i.endswith("9.txt"):
        pres_names.add(i[:-5].split("_")[-1])
    elif i[:-4].split("_")[-1]:
        pres_names.add(i[:-4].split("_")[-1])

    # Convert the speeches in lowercase, remove the punctuation and store them in the directory ./cleaned
    with open(f"./speeches/{i}", 'r', encoding='utf-8') as f1:
        with open(f"./cleaned/{i}", 'w', encoding='utf-8') as f2:
            for i in f1.read():
                if ord(i) >= 48 and ord(i) <= 57 or ord(i) >= 65 and ord(i) <= 90 or ord(i) >= 97 and ord(i) <= 122:
                    f2.write(i.lower())

                if not (ord(i) >= 48 and ord(i) <= 57 or ord(i) >= 65 and ord(i) <= 90 or ord(i) >= 97 and ord(
                        i) <= 122):
                    if ord(i) > 127:
                        f2.write(i)
                    else:
                        f2.write(" ")


list_of_files("./Cleaned", ".txt")


# + TF-IDF


def tf(string):
    occurences = {}
    word = ""
    i = 0
    while i < (len(string)):
        if string[i] == " " or word[:2] == "\n":
            word = word.replace("\n","")
            if word in occurences:
                occurences[word] += 1
            else:
                occurences[word] = 1
            word = ""
            i += 1
        else:
            word += string[i]
            i += 1
    if word in occurences:
        occurences[word] += 1
    else:
        occurences[word] = 1
    return occurences


def idf(corpus):
    words_in_corpus = {}
    for filename in os.listdir(corpus):
        with open("Cleaned/"+filename, "r", encoding="utf-8") as f:
            words = tf(f.read())
            for word in words:
                if word in words_in_corpus:
                    words_in_corpus[word] += 1
                else:
                    words_in_corpus[word] = 1
    for word in words_in_corpus:
        words_in_corpus[word] = math.log(8/words_in_corpus[word])
    return words_in_corpus


def tf_idf(directory):
    idf_score = idf(directory)
    tf_idf_matrix = []
    for el in idf_score:
        tf_idf_matrix.append([el])
    for i in range(len(tf_idf_matrix)):
        for j in range(8):
            tf_idf_matrix[i].append(0)
    y = 1
    for filename in os.listdir(directory):
        tf_dic = {}
        with open("Cleaned/"+filename, "r", encoding="utf-8") as f:
            tf_dic = tf(f.read())
        i = 0
        for el in idf_score:
            if el in tf_dic:
                tf_idf_matrix[i][y] = tf_dic[el]*idf_score[el]
            i += 1
        y += 1
    return tf_idf_matrix


def least_important():
    matrix = tf_idf("./Cleaned")
    list_words = []
    for i in range(len(matrix)):
        unimportant = True
        j = 1
        while unimportant and j<len(matrix[i]):
            if matrix[i][j] != 0:
                unimportant = False
            else:
                j += 1
        if unimportant == True:
            list_words.append(matrix[i][0])
    return list_words


def highest_tf_idf():
    matrix = tf_idf("./Cleaned")
    list_words = []
    max = 0

    for i in range(len(matrix)):
        for j in range(1,9):
            if matrix[i][j] > max:
                max = matrix[i][j]
    for i in range(len(matrix)):
        highest = False
        j = 1
        while not highest and j<9:
            if matrix[i][j] == max:
                highest = True
                list_words.append(matrix[i][0])
            else:
                j += 1
    return list_words


def most_repeated_word(name):
    files_names = []
    text = ""
    for filename in os.listdir("./Cleaned"):
        if filename.endswith(".txt"):
            files_names.append(filename)
    for i in range(len(files_names)):
        if name in files_names[i]:
            with open("Cleaned/" + files_names[i], "r", encoding="utf-8") as f:
                text += f.read()+" "
    words = tf(text)
    max = 0
    list_word = []
    for el in words:
        if words[el] > max:
            max = words[el]
    for el in words:
        if words[el] == max:
            list_word.append(el)
    print(words)
    return list_word


def search_who_said(word):
    files_names = []
    names = set()
    highest_user = ""
    max = 0
    pres = ""
    for filename in os.listdir("./Cleaned"):
        if filename.endswith(".txt"):
            files_names.append(filename)
    for i in range(len(files_names)):
        with open("Cleaned/" + files_names[i], "r", encoding="utf-8") as f:
            words_said = tf(f.read())
        if word in words_said:
            for el in pres_names:
                if el in files_names[i]:
                    names.add(el)
                    pres = el
            if words_said[word] > max:
                max = words_said[word]
                highest_user = pres
    if names == set():
        return "no one said that"
    else:
        return ("here are all president who said it:",names,
                "and here is the president who said it the most times:",highest_user)


def commonWords():
    common_words = []
    total_words = tf_idf("./Cleaned")
    files_names = []
    for filename in os.listdir("./Cleaned"):
        if filename.endswith(".txt"):
            files_names.append(filename)

    for el in total_words:
        counter_president = 0

        for i in range(len(pres_names)):
            text = " "

            for j in range(len(files_names)):
                if list(pres_names)[i] in files_names[j]:
                    with open("Cleaned/" + files_names[j], "r", encoding="utf-8") as f:
                        text += f.read() + " "
            words = tf(text)
            if el[0] in words:
                counter_president += 1
        if counter_president == 6 and el[0] not in least_important():
            common_words.append(el[0])
    return common_words


def menu():
    welcome = """Welcome user, I am a chat bot that allow you to get informations about some french presidents' speeches of their nomination.
          First, you have to choose which action you want to procceed. To do so enter the corresponding number and follow the instructions.

          [1] : Display a list of the least important words in all speeches combined
          [2] : Display a list of the most important words all speeches combined
          [3] : Display the most said words for a given president
          [4] : Display the name of all the president who talked about a given word and the first one who did it
          [5] : Display a list of the files that are analysed to prived the answers
          [6] : Display all words that every presidents said but which aren't in the list of least important words
          [7] : Display this list another time
          [8] : Close the program

          """
    print(welcome)
    while True:
        choice = int(input("Make your choice : "))

        if choice == 1:
            print(least_important())
        elif choice == 2:
            print(highest_tf_idf())
        elif choice == 3:
            name = str(input("Choose a president name :"))
            print(most_repeated_word(name))
        elif choice == 4:
            word = str(input("Choose a word to find"))
            print(search_who_said(word))
        elif choice == 5:
            print(files_names)
        elif choice == 6:
            print(commonWords())
        elif choice == 7:
            print(welcome)
        elif choice == 8:
            return "Goodbye"
        else:
            print("The number you entered is not valid")

