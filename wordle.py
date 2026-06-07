import random,wordlehelper
from collections import Counter


def wordselect():
    with open("everywordleword.txt","r") as file:
        data = file.readlines()[0].strip(",").split(",")
        file.close()

    word = data[random.randint(0,len(data)-1)]
    return word

def hangmanmain(word):
    # main program
    # print("Chose and option: Start the game (A), Add a new word (B), Exit (C)")
    # choice = input(": ")
    greenfile = open("greenletters.txt","a")
    yellowfile = open("yellowletters.txt","a")
    grayfile = open("grayletters.txt","a")
    lives = 5
    score = 0
    guesses = []
    greenletters = []
    yellowletters = []
    grayletters = []
    greenPos = []
    yellowAntiPos = []
    numbers = ['0', '2', '3', '4', '5', '6', '7', '8', '9']

    cipher = ["_"] * len(word)
    print("the word has", len(word), "characters")
    print("the word is", word)
    wordCounts = Counter(word)

    while lives >= 0:  # similar to pacman coin system
        for carrier in greenletters:
            grayletters = wordlehelper.remove1D(grayletters,carrier)
        for carrier in yellowletters:
            grayletters = wordlehelper.remove1D(grayletters,carrier)
        yellowString = ""
        for group in yellowAntiPos:
            for pos in group:
                yellowString += str(pos)
            yellowString += ","
        greenstring = ""
        for pos in greenPos:
            greenstring += str(pos)
        userInput = wordlehelper.main(yellowletters,yellowString,greenletters,greenstring,grayletters).lower()

        if userInput == '1':  # quit game
            return (-9999999999)

        if userInput == '2':
            print("Word Skipped")
            lives = -1

        numbersPresent = False
        for carrier in userInput:
            if carrier in numbers:
                numbersPresent = True
                break

        if userInput == "":
            continue
        elif userInput in guesses:
            print("The word was already guessed")
        elif numbersPresent:
            print("Numbers present in guess...")
        elif len(word) == 5:
            guesses.append(userInput)
            lives -= 1
            for carrier in range(5):
                if userInput[carrier] == word[carrier]:
                    score += 10  # no need to check for repeated inputs that force more points. This is because of prerequisite check of 'if word in guesses:'
                    cipher[carrier] = word[carrier]
                    if userInput[carrier] in greenletters.append(userInput[carrier]) and wordCounts[userInput[carrier]] - greenletters.count(userInput[carrier]) > 0:
                        greenletters.append(userInput[carrier])
                        greenPos.append(carrier)
                elif userInput[carrier] != word[carrier] and userInput[carrier] in word and wordCounts[userInput[carrier]] - (greenletters.count(userInput[carrier]) + yellowletters.count(userInput[carrier])) > 0:
                    if userInput[carrier] in yellowletters:
                        yellowAntiPos[yellowletters.index(userInput[carrier])].append(carrier)
                    else:
                        yellowletters.append(userInput[carrier])
                    yellowAntiPos.append([carrier])
                elif userInput[carrier] not in word:
                    grayletters.append(userInput[carrier])

            print(cipher)  # print new cipher only

        else:
            print("word does not have enough letters")

    print("The word was", str(word))
    print(score)
    return (score)

def scoresandnames(score):
    if score == -9999999999:
        return (-1)  # tells game to quit in main game loop

    print("upload score?")
    scoreupload = input("(Y/N)>>")
    if scoreupload.upper() == "YES" or scoreupload.upper() == "Y":
        username = input("Input Username:")
        file = open("TABLEOFSCORES.txt", "a")
        troll = [["The user known as:", 0.2], ["The idiot called", 0.1], ["This dead guy -->", 0.2],
                 ["Number #1 player:", 0.01], ["The user by the name of:", 0.9]]
        total_probability = 0
        for placeholder in troll:
            total_probability += placeholder[1]
        random_value = random.random() * total_probability
        cumulative_probability = 0
        prename_text = ""
        for placeholder in troll:
            cumulative_probability += placeholder[1]
            if random_value < cumulative_probability:
                prename_text = placeholder[0]
                break

        post_texts = [["a weak score of:", 0.2], ["a really bad score of:", 0.1], ["an amazing score of:", 0.2],
                      ["Number #1 player:", 0.01], ["The user by the name of:", 0.9]]
        total_probability = 0
        for placeholder in post_texts:
            total_probability += placeholder[1]
        random_value = random.random() * total_probability
        cumulative_probability = 0
        postname_text = ""
        for placeholder in post_texts:
            cumulative_probability += placeholder[1]
            if random_value < cumulative_probability:
                postname_text = placeholder[0]
                break

        write_data = str(prename_text + " " + username + " has scored " + postname_text + " " + str(score) + "\n")
        file.write(write_data)
        file.close()
        return (1)  # shows operation was successful
    else:
        return (2)  # shows operation was successful (alternate operation)
        pass


# main game loop
while True:
    semaphore = scoresandnames(hangmanmain(wordselect()))
    if semaphore == -1:
        break
    elif semaphore == 1:
        print("Saved...")
    elif semaphore == 2:
        print("Not saved...")