import tfIdf

def unimportantWords(corpus):
    words = []
    for word in tfIdf.idf(corpus).keys():
        if tfIdf.idf(corpus)[word] == 0:
            words.append(word)
    return(words)

def highestTfIdf(corpus):
    value = 0
    listOfWords = []
    for files in tfIdf.list_of_files("./cleaned"):
        for i in tfIdf.tf(f"{corpus}/{files}"):
            if tfIdf.final_score(corpus, files, i) == value:
                listOfWords.append(i)
            elif tfIdf.final_score(corpus, files, i) > value:
                value = tfIdf.final_score(corpus, files, i)
                listOfWords = []
                listOfWords.append(i)
    return(listOfWords)

def mostRepeatedWord(name):
    listWords = []
    mostValue = 0
    for i in tfIdf.list_of_files("./cleaned"):
        print(i)
        if name in i:
            for key, value in tfIdf.tf(f"./cleaned/{i}").items():
                if value == mostValue:
                    listWords.append(key)
                elif value > mostValue:
                    mostValue = value
                    listWords = []
                    listWords.append(key)
    return(listWords)

def listNames(word):
    listNames = []
    for i in tfIdf.list_of_files("./cleaned"):
        if word in tfIdf.tf(f"./cleaned/{i}"):
            if i.endswith("0.txt") or i.endswith("1.txt") or i.endswith("2.txt") or i.endswith("3.txt") or i.endswith("4.txt") or i.endswith("5.txt") or i.endswith("6.txt") or i.endswith("7.txt") or i.endswith("8.txt") or i.endswith("9.txt"):
                if i[:-5].split("_")[-1] not in listNames:
                    listNames.append(i[:-5].split("_")[-1])
            elif i[:-4].split("_")[-1] not in listNames:
                if i[:-5].split("_")[-1] not in listNames:
                    listNames.append(i[:-4].split("_")[-1])
    return(listNames)

def mostName(word):
    value = 0
    mostValue = 0
    name = ""
    for i in tfIdf.list_of_files("./cleaned"):
        if word in tfIdf.tf(f"./cleaned/{i}"):
            value = tfIdf.tf(f"./cleaned/{i}")[word]
            if value > mostValue:
                if i.endswith("0.txt") or i.endswith("1.txt") or i.endswith("2.txt") or i.endswith("3.txt") or i.endswith("4.txt") or i.endswith("5.txt") or i.endswith("6.txt") or i.endswith("7.txt") or i.endswith("8.txt") or i.endswith("9.txt"):
                    name = i[:-5].split("_")[-1]
                elif i[:-4].split("_")[-1]:
                    name = i[:-4].split("_")[-1]
    return(name)
    
def firstTo(word):
    chronoList = ['dEstaing', 'Mitterrand', 'Chirac', 'Sarkozy', 'Hollande', 'Macron']
    value = None
    name = ''
    for i in tfIdf.list_of_files("./cleaned"):
        if word in tfIdf.tf(f"./cleaned/{i}"):
            if i.endswith("0.txt") or i.endswith("1.txt") or i.endswith("2.txt") or i.endswith("3.txt") or i.endswith("4.txt") or i.endswith("5.txt") or i.endswith("6.txt") or i.endswith("7.txt") or i.endswith("8.txt") or i.endswith("9.txt"):
                if value == None or value > chronoList.index(i[:-5].split("_")[-1]):
                    value = chronoList.index(i[:-5].split("_")[-1])
            elif i[:-4].split("_")[-1]:
                if value == None or value > chronoList.index(i[:-4].split("_")[-1]):
                    value = chronoList.index(i[:-4].split("_")[-1])
    return(chronoList[value])