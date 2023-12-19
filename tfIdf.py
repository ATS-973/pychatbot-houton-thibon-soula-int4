import os
import math

def list_of_files(corpus, extension): # Return all the name of files in the given directory with a specific extension
    files = []
    for filename in os.listdir(corpus):
        if filename.endswith(extension):
            files.append(filename)
    return files

def tf(pathOfFile):  # Return a dictionnary with the Tf score of each word for a given document
    with open(pathOfFile, 'r', encoding='utf-8') as f1:
        wordsOcc = {}
        for i in f1.read().split(" "):
            if i == "":
                pass
            else:
                if i not in wordsOcc:
                    wordsOcc[i] = 1
                else:
                    wordsOcc[i] += 1
    return(wordsOcc)

def idf(corpus):  # Return a dictionnary with the idf score of each word for a given folder of text documents
    wordsOcc = {}
    for i in os.listdir(corpus):
        for key in tf(f"{corpus}/{i}").keys():
            if key not in wordsOcc:
                wordsOcc[key] = 1
            else:
                wordsOcc[key] += 1
    for key in wordsOcc.keys():
        wordsOcc[key] = math.log(8/wordsOcc[key],10)
    return(wordsOcc)

def final_score(corpus, files, word):  # Return the Tf-Idf score of a given word for a given directory and a given file
    wordsOccIdf = idf(corpus)
    score = ""
    for key,value in tf(f"{corpus}/{files}").items():
        if key == word:
            score = value * wordsOccIdf[key]
    return(score)

def matrice(corpus):  # Return the Tf-Idf matrix of a given corpus of document
    wordsOccIdf = idf(corpus)
    listFiles = list_of_files(corpus, "txt")
    mat = []
    for key in wordsOccIdf.keys():
        row = []
        nb_i = 0
        for i in os.listdir(corpus):
            if key not in tf(f"{corpus}/{listFiles[nb_i]}").keys():
                row.append(0)
            else:
                row.append(final_score("./cleaned", i, key))
            nb_i += 1
        mat.append(row)
    return(mat)
