def hangMan(word):
    wrong=0

    stages = [
             "_________       ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
              ]

    wList = list(word)
    board = ["_"] * len(word)
    uniqCount = len(set(word))

    print("\n")
    print("Welcome to Hangman game")
    win = False

    while wrong < len(stages):

        print("\n")
        guessL = input("Guess a Letter: ")

        if guessL in wList:
            print("Good guess. {} is in the word".format(guessL))

            for idx,val in enumerate(wList):
                if val == guessL:
                    wList[idx] = "$"
                    board[idx] = guessL

            if ("".join(board) == word):
                print ("\nYou win. {} is the word.".format(word))
                win = True
                break
            else:
                print (" ".join(board))
  
        else:
            print("\nWrong guess. {} is not in the word".format(guessL))
            wrong += 1
            print (" ".join(board))
            print("\n")
            print("\n".join(stages[0:wrong]))

    if not win:
        print ("\nYou lose. {} was the word".format(word))
    
    

hangMan("superstitious")

