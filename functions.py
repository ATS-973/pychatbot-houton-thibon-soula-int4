import tfIdf

def unimportantWords(corpus):
    words = []
    for word in tfIdf.idf(corpus).keys():
        if tfIdf.idf(corpus)[word] == 0:
            words.append(word)
    return(words)