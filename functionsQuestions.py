import tfIdf
import math

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
    questionCleared = [i for i in questionCleared if i != ""]
    return(questionCleared)

def wordsInCorpus(corpus, question):
    questionCleared = tokenization(question)
    idfList = tfIdf.idf(corpus).keys()
    finalWords = []
    for i in questionCleared:
        if i in idfList:
            finalWords.append(i)
    return(finalWords)

def tfIdfQuestion(corpus, question):
    wordsOcc = {}
    idfCorpus = tfIdf.idf(corpus)
    vector = []
    for i in wordsInCorpus("./cleaned", question):
        if i not in wordsOcc:
            wordsOcc[i] = 1
        else:
            wordsOcc[i] += 1
    for key,value in wordsOcc.items():
        wordsOcc[key] = 1/value
    for i in idfCorpus:
        if i in wordsOcc:
            vector.append(wordsOcc[i]*idfCorpus[i])
        else:
            vector.append(0)
        
    return(vector)

def scalarProduct(vectorA, vectorB):
    scalarProduct = 0
    for i in range(0, len(vectorA)-1, 1):
        scalarProduct += vectorA[i] * vectorB[i]
    return(scalarProduct)

def normeVector(vector):
    norme = 0
    for i in vector:
        norme += i**2
    return(math.sqrt(norme))

def similarity(vectorA, vectorB):
    score = scalarProduct(vectorA, vectorB) / (normeVector(vectorA) * normeVector(vectorB))
    return(score)

def mostReleventDoc(corpus, question):
    matriceIdf = tfIdf.matrice(corpus)
    docVect = tfIdfQuestion(corpus, question)
    vectDocIdf = []
    actScore = 0
    maxScore = 0
    releventDoc = None
    for i in range(0, len(tfIdf.list_of_files(corpus, ".txt")), 1):
        for element in matriceIdf:
            vectDocIdf.append(matriceIdf[matriceIdf.index(element)][i])
        
        actScore = similarity(docVect, vectDocIdf)

        if actScore > maxScore:
            releventDoc = i
            maxScore = actScore

        vectDocIdf = []
    
    return(tfIdf.list_of_files(corpus, ".txt")[releventDoc])

def answer(corpus, question):
    maxi = 0
    idfCorpus = list(tfIdf.idf(corpus))
    tfIdfScore = tfIdfQuestion("./cleaned",question)
    for value in tfIdfScore:
        if value > maxi:
            maxi = value

    answer = ""
    firstOcc = 0
    startSent = 0
    endSent = 0
    final_answer = ""
    with open(f"./speeches/{mostReleventDoc(corpus, question)}", "r", encoding="utf-8") as f1:
        texte = f1.read().split()
        while texte[firstOcc] != idfCorpus[tfIdfScore.index(maxi)]:
            firstOcc += 1
        ponctuation = [".", "!", "?"]
        for i in range(firstOcc, 0, -1):
            if texte[i-1][-1] in ponctuation and startSent == 0:
                startSent = i
        for i in range(firstOcc, len(texte), 1):
            if texte[i].split("\n")[0][-1] in ponctuation and endSent == 0:
                endSent = i
        for i in range(startSent, endSent, 1):
            answer += texte[i] + " "
        answer += texte[endSent].split("\n")[0]
        answer = chr(ord(answer[0])+32)+answer[1:]

    question_starters = {
        "Comment": "Après analyse, ",
        "Pourquoi": "Car, ",
        "Peux-tu": "Oui, bien sûr! "
    }

    for i in question_starters:
        if question.startswith(i):
            final_answer = question_starters[i]+answer
            break
    if final_answer != "":
        return(final_answer)
    else:
        return(answer)