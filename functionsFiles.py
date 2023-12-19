import tfIdf
import os

def initialisation():   # Create the ./cleaned directory if not exists and transform all txt files with no uppercase letters and no ponctuation
    pres_names = set()

    if os.path.isdir("./cleaned") == False:
        os.mkdir("./cleaned")

    for i in tfIdf.list_of_files("./speeches","txt"): #Get all the presiden names from the speeches files in the speeches directory
        if i.endswith("0.txt") or i.endswith("1.txt") or i.endswith("2.txt") or i.endswith("3.txt") or i.endswith("4.txt") or i.endswith("5.txt") or i.endswith("6.txt") or i.endswith("7.txt") or i.endswith("8.txt") or i.endswith("9.txt"):
            pres_names.add(i[:-5].split("_")[-1])
        elif i[:-4].split("_")[-1]:
            pres_names.add(i[:-4].split("_")[-1])
        
        #Convert the speeches in lowercase, remove the punctuation and store them in the directory ./cleaned
        with open(f"./speeches/{i}", 'r', encoding='utf-8') as f1:
            with open(f"./cleaned/{i}",'w', encoding='utf-8') as f2:
                for i in f1.read():
                    if ord(i) >= 48 and ord(i) <= 57 or ord(i)>=65 and ord(i)<= 90 or ord(i) >= 97 and ord(i) <= 122:
                        if ord(i)>=65 and ord(i)<=90:
                            f2.write(chr(ord(i)+32))
                        elif ord(i) >= 48 and ord(i) <= 57 or ord(i) >= 97 and ord(i) <= 122:
                            f2.write(i)

                    if not(ord(i) >= 48 and ord(i) <= 57 or ord(i) >= 65 and ord(i) <= 90 or ord(i) >= 97 and ord(i) <= 122):
                        if ord(i) > 127:
                            f2.write(i)
                        else:
                            f2.write(" ")

def unimportantWords(corpus):   # Return all the "unimportant" words according to their tf score
    words = []
    listWords = tfIdf.idf(corpus).keys()
    for word in listWords:
        if tfIdf.idf(corpus)[word] == 0:
            words.append(word)
    return(words)

def highestTfIdf(corpus):  # Return the word(s) with the highest TfIdf score in the corpus
    value = 0
    listOfWords = []
    for files in tfIdf.list_of_files("./cleaned", "txt"):
        for i in tfIdf.tf(f"{corpus}/{files}"):
            if tfIdf.final_score(corpus, files, i) == value:
                listOfWords.append(i)
            elif tfIdf.final_score(corpus, files, i) > value:
                value = tfIdf.final_score(corpus, files, i)
                listOfWords = []
                listOfWords.append(i)
    return(listOfWords)

def mostRepeatedWord(name):   # Return the most repeated word(s) by a given president
    forgetable = unimportantWords("./cleaned")
    listWords = []
    mostValue = 0
    for i in tfIdf.list_of_files("./cleaned", "txt"):
        if name in i:
            for key, value in tfIdf.tf(f"./cleaned/{i}").items():
                if value == mostValue and key not in forgetable:
                    listWords.append(key)
                elif value > mostValue and key not in forgetable:
                    mostValue = value
                    listWords = []
                    listWords.append(key)
    return(listWords)

def listNames(word):  # Return the list of all president who talked about a given word
    listNames = []
    for i in tfIdf.list_of_files("./cleaned" , "txt"):
        if word in tfIdf.tf(f"./cleaned/{i}"):
            if i.endswith("0.txt") or i.endswith("1.txt") or i.endswith("2.txt") or i.endswith("3.txt") or i.endswith("4.txt") or i.endswith("5.txt") or i.endswith("6.txt") or i.endswith("7.txt") or i.endswith("8.txt") or i.endswith("9.txt"):
                if i[:-5].split("_")[-1] not in listNames:
                    listNames.append(i[:-5].split("_")[-1])
            elif i[:-4].split("_")[-1] not in listNames:
                if i[:-5].split("_")[-1] not in listNames:
                    listNames.append(i[:-4].split("_")[-1])
    return(listNames)

def mostName(word):  # Return the name of the president who talked the most about a given word
    value = 0
    mostValue = 0
    name = ""
    for i in tfIdf.list_of_files("./cleaned", "txt"):
        if word in tfIdf.tf(f"./cleaned/{i}"):
            value = tfIdf.tf(f"./cleaned/{i}")[word]
            if value > mostValue:
                if i.endswith("0.txt") or i.endswith("1.txt") or i.endswith("2.txt") or i.endswith("3.txt") or i.endswith("4.txt") or i.endswith("5.txt") or i.endswith("6.txt") or i.endswith("7.txt") or i.endswith("8.txt") or i.endswith("9.txt"):
                    name = i[:-5].split("_")[-1]
                elif i[:-4].split("_")[-1]:
                    name = i[:-4].split("_")[-1]
    return(name)
    
def firstTo(word):  # Return the name of the president who first talked about a given word
    chronoList = ['dEstaing', 'Mitterrand', 'Chirac', 'Sarkozy', 'Hollande', 'Macron']
    value = -1
    for i in tfIdf.list_of_files("./cleaned", "txt"):
        for j in tfIdf.tf(f"./cleaned/{i}"):
            if word in j:
                if i.endswith("0.txt") or i.endswith("1.txt") or i.endswith("2.txt") or i.endswith("3.txt") or i.endswith("4.txt") or i.endswith("5.txt") or i.endswith("6.txt") or i.endswith("7.txt") or i.endswith("8.txt") or i.endswith("9.txt"):
                    if value == -1 or value > chronoList.index(i[:-5].split("_")[-1]):
                        value = chronoList.index(i[:-5].split("_")[-1])
                elif i[:-4].split("_")[-1]:
                    if value == -1 or value > chronoList.index(i[:-4].split("_")[-1]):
                        value = chronoList.index(i[:-4].split("_")[-1])
    if value >= 0 and value <= len(chronoList):
        return(chronoList[value])
    else:
        return("No president talked about the word you gave")