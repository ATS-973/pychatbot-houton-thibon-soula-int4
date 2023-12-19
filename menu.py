import functionsFiles
import tfIdf
import functionsQuestions

def menu():
    welcome = """
    Welcome user, I am a chat bot that allow you to get informations about some french presidents' speeches of their nomination.
          First, you have to choose which action you want to procceed. To do so enter the corresponding number and follow the instructions.
          
          [1] : Display a list of the least important words in all speeches combined
          [2] : Display a list of the most important words all speeches combined
          [3] : Display the most said words for a given president
          [4] : Display the names of all the president who talked about a given word
          [5] : Display the name of the first president who talked about a given word
          [6] : Display a list of the files that are analysed to provived the answers
          [7] : Display this list another time
          [8] : Enter ChatBot mode : Ask your own question and get approximative answers !
          [9] : Close 
          
          """
    print(welcome)
    while True:
        choice = int(input("Make your choice : "))

        if choice == 1:
            print("Processing...")
            print()
            print(functionsFiles.unimportantWords('./cleaned'))
            print()
            print("#########################################################")
            print()
        elif choice == 2:
            print("Processing...")
            print()
            print(functionsFiles.highestTfIdf('./cleaned'))
            print()
            print("#########################################################")
            print()
        elif choice == 3:
            name = str(input("Choose a president name : "))
            print("Processing...")
            print()
            print(f"The most reapeted words are {functionsFiles.mostRepeatedWord(name)}")
            print()
            print("#########################################################")
            print()
        elif choice == 4:
            word = str(input("Choose a word to find : "))
            print("Processing...")
            print()
            print(functionsFiles.listNames(word))
            print()
            print("#########################################################")
            print()
        elif choice == 5:
            word = str(input("Choose a word to find : "))
            print("Processing...")
            print()
            print(functionsFiles.firstTo(word))
            print()
            print("#########################################################")
            print()
        elif choice == 6:
            print("Processing...")
            print()
            print(tfIdf.list_of_files("./cleaned", ".txt"))
            print()
            print("#########################################################")
            print()
        elif choice == 7:
            print(welcome)
        elif choice == 8:
            question = str(input("Enter the question you want to ask (in french): "))
            print("Processing...")
            print()
            print(functionsQuestions.answer("./cleaned", question))
            print()
            print("#########################################################")
            print()
        elif choice == 9:
            print("Good bye")
            print()
            print("#########################################################")
            print()
            exit()
        else:
            print("The number you entered is not valid")
