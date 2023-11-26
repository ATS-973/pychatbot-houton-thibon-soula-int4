import os
import math

def list_of_files(corpus):
    list = []
    for i in os.listdir(corpus):
        list.append(i)
    return(list)

def tf(pathOfFile):
    with open(pathOfFile, 'r', encoding='utf-8') as file:
        wordsOcc = {}
        for i in file.read().split(" "):
            if i == "":
                pass
            else:
                if i not in wordsOcc:
                    wordsOcc[i] = 1
                else:
                    wordsOcc[i] += 1
    return(wordsOcc)

def idf(corpus):
    wordsOcc = {}
    for i in os.listdir(corpus):
        for key in tf(f"{corpus}/{i}").keys():
            if key not in wordsOcc:
                wordsOcc[key] = 1
            else:
                wordsOcc[key] += 1
    for key in tf(f"{corpus}/{i}").keys():
        wordsOcc[key] = math.log(8/wordsOcc[key])
    return(wordsOcc)

def final_score(corpus, file, word):
    score = {}
    for key in tf(f"{corpus}/{file}").keys():
        score[key] = tf(f"{corpus}/{file}")[key] * idf(corpus)[key]
    return(score[word])

def matrice(corpus):
    mat = []
    for key in idf(corpus).keys():
        row = []
        nb_i = 0
        for i in os.listdir(corpus):
            if key not in tf(f"{corpus}/{list_of_files(corpus)[nb_i]}").keys():
                row.append(0)
            else:
                row.append(tf(f"{corpus}/{list_of_files(corpus)[nb_i]}")[key])
            nb_i += 1
        mat.append(row)
    return(mat)
