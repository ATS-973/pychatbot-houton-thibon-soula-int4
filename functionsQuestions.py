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

