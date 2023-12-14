import tfIdf
import os

def tokenization(question):
    questionCleared = ""
    for i in question:
        if ord(i) >= 48 and ord(i) <= 57 or ord(i)>=65 and ord(i)<= 90 or ord(i) >= 97 and ord(i) <= 122:
            if ord(i)>=65 and ord(i)<=90:
                questionCleared += chr(ord(i)+32)
            elif ord(i) >= 48 and ord(i) <= 57 or ord(i) >= 97 and ord(i) <= 122:
                questionCleared += i

        if not(ord(i) >= 48 and ord(i) <= 57 or ord(i) >= 65 and ord(i) <= 90 or ord(i) >= 97 and ord(i) <= 122):
            if ord(i) > 127:
                questionCleared += i
            else:
                questionCleared += " "
    questionCleared = questionCleared.split(" ")
    return(questionCleared)

def wordsInCorpus(corpus, question):
    questionCleared = tokenization(question)
    idfList = tfIdf.idf(corpus).keys()
    finalWords = []
    for i in questionCleared:
        if i in idfList:
            finalWords.append(i)
    return(finalWords)

def tfQuestion(question):
    wordsOcc = {}
    for i in tokenization(question):
        if i not in wordsOcc:
            wordsOcc[i] = 1
        else:
            wordsOcc[i] += 1
    for key,value in wordsOcc.items():
        wordsOcc[key] = 1/value
        
    return(wordsOcc)

def matriceQuestion(question, corpus):
    matQuestion = []
    mat = tfIdf.matrice(corpus)
    idfCorpus = tfIdf.idf(corpus)
    for i in tokenization(question):
        if i in idfCorpus.keys():
            matQuestion.append(mat[list(idfCorpus.keys()).index(i)])
    return(matQuestion)

