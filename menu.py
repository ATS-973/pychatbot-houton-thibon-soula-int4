import functionsFiles
import tfIdf
import functionsQuestions

def menu():
    welcome = """Welcom user, I am a chat bot that allow you to get informations about some french presidents' speeches of their nomination.
          First, you have to choose which action you want to procceed. To do so enter the corresponding number and follow the instructions.
          
          [1] : Display a list of the least important words in all speeches combined
          [2] : Display a list of the most important words all speeches combined
          [3] : Display the most said words for a given president
          [4] : Display the names of all the president who talked about a given word
          [5] : Display the name of the first president who talked about a given word
          [6] : Display a list of the words that all presidents mention at least once (except for the least inportant words)
          [7] : Display a list of the files that are analysed to provived the answers
          [8] : Display this list another time
          [9] : Enter ChatBot mode : Ask your own question and get approximative answers !
          [10] : Close 
          
          """
    print(welcome)
    while True:
        choice = int(input("Make your choice : "))

        if choice == 1:
            print("Processing...")
            print(functionsFiles.unimportantWords('./cleaned'))
        elif choice == 2:
            print("Processing...")
            print(functionsFiles.highestTfIdf('./cleaned'))
        elif choice == 3:
            name = str(input("Choose a president name : "))
            print("Processing...")
            print(f"The most reapeted words are {functionsFiles.mostRepeatedWord(name)}")
        elif choice == 4:
            word = str(input("Choose a word to find : "))
            print("Processing...")
            print(functionsFiles.listNames(word))
        elif choice == 5:
            word = str(input("Choose a word to find : "))
            print("Processing...")
            print(functionsFiles.firstTo(word))
        elif choice == 6:
            print("Processing...")
            #print(test.commonWords())
        elif choice == 7:
            print("Processing...")
            print(tfIdf.list_of_files("./cleaned"))
        elif choice == 8:
            print(welcome)
        elif choice == 9:
            question = str(input("Enter the question you want to ask (in french): "))
            print("Processing...")
            print(functionsQuestions.answer("./cleaned", question))
        elif choice == 10:
            print("Good bye")
            exit()
        else:
            print("The number you entered is not valid")
