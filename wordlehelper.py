import itertools,string,enchant,math
import tkinter

def remove1D(list1, target):#removes target elem, in a given 1D list/array
    new_list = []
    for carrier in list1:
        if carrier == target:
            pass
        else:
            new_list.append(carrier)
    return new_list

def removeDuplicateElements(list1):
    return list(dict.fromkeys(list1))

def pressedEnter():
    global yellow_letters_input, yellow_letter_positions_anti_input, green_letters_input, green_letter_positions_input, gray_letters_input, yellow_let_tk, yellow_pos_tk, green_tk, greenp_tk, gray_tk, window

    yellow_letters_input = yellow_let_tk.get().strip()
    yellow_letter_positions_anti_input = yellow_pos_tk.get().strip()
    green_letters_input = green_tk.get().strip()
    green_letter_positions_input = greenp_tk.get().strip()
    gray_letters_input = gray_tk.get().strip()

    window.destroy()


def main(yellowExternalBypass=None, yellowAntiPosExternalBypass=None, greenExternalBypass=None, greenPosExternalBypass=None, grayExternalBypass=None):
    global yellow_letters_input, yellow_letter_positions_anti_input, green_letters_input, green_letter_positions_input, gray_letters_input, yellow_let_tk, yellow_pos_tk, green_tk, greenp_tk, gray_tk, window

    # Define all characters to use in the password
    chars = string.ascii_lowercase

    # Define MAX_LEN, min_value length and passwordfound
    beginningPartial = ""
    MAX_LEN = 5
    min_value = MAX_LEN - len(beginningPartial)

    #list for comparison of values to see what is a word
    possible_combos=[]

    #it is faster to use pregenerated data (exponential generation should be cached - basically, cache brute-force data)
    preloadedCombos = []

    with open("everywordleword.txt","r") as f:
        preloadedCombos = f.readlines()[0].strip(",").split(",")
        f.close()

    # preloadedCombos = itertools.combinations(data,len(data)) idk check it out later, never done it like this
    if len(preloadedCombos) >= math.pow(5,5):
        for carrier in range(len(preloadedCombos)):
            if preloadedCombos[carrier][:len(beginningPartial)] == beginningPartial: #list[wordNo][string_index] is basically subStringing it (thanks, Chang-Qi)
                #what it does is choose the word from the list so list1 = ["hello", "my", "name", "is", "Yusuf"] and basically first is choosing the word - understandable
                #but as you can manip strings like lists in python (e.g: for carrier in "exampleWord": or word = "thisIsAWord" ... for carrier in word:)
                #we can then use the [:n] notation where n is an integer representing the exclusive end range limit. As it is a string, not a list, the returned element fragment is...
                #a string fragment, not a fragment of a list -> ["hello", "my"] vs "hel"
                possible_combos.append(preloadedCombos[carrier])
            else:
                pass

    else: #brute force the list of all chars, then only save to memory those words that match the beginning partial string match stored in var:beginningPartial

        # Try all possible combinations of characters up to MAX_LEN
        for length in range(min_value, min_value + 1):
            for combination in itertools.product(chars, repeat=length):

                # Join the characters in the combination to form a partial word candidate
                candidate = "".join(combination)
                possible_combos.append(str(beginningPartial+candidate))
        #generate all possible combos

#here to avoid ref before assignment (different flows could prevent creation, for exmaple, if called externally, the below if won't run and create the 5 vars
    yellow_letters_input = ""
    yellow_letter_positions_anti_input = ""
    green_letters_input = ""
    green_letter_positions_input = ""
    gray_letters_input = ""

    if yellowExternalBypass == None and yellowAntiPosExternalBypass == None and greenExternalBypass == None and greenPosExternalBypass == None and grayExternalBypass == None:

        if input("type Y for quick readme, or any input to continue:").lower() == "y":
            input("""For general use, and to avoid confusion, letter positions start at 1 and end at 5.\n\nFor example, the word 'Hello' would have 'H' at position 1 and 'O' at position 5.
            Letters for inputs and numbers for green letters positions can be comma separated, however, this is unnecessary.
            
            Yellow positions, however, will need to be separated by commas, but only between letters.
            For example, if a letter is not in position 3 (yellow letter shows the word is not at this position) then we do 3 for the input, and in the order of how we typed it.
            
            Enter yellow letters: y,t
            Enter anti positions: 2345,123
            
            This will then be encoded as:
            [[2,3,4,5],[1,2,3]]
            
            Only yellow letters have this added complexity. Green letters can be written as is, in order, and will code as so:
            
            Enter green letters: a,b
            Enter positions: 15
            
            This will then be encoded as:
            [1,5]
            
            This will tell the program that there is an 'a' at the beginning and a 'b' at the end of the word
            Case does not matter. All words are put into lowercase. Inputs are processed immediately and lowered into lowercase#
            All inputs need to be put in order of the letters given. This only matters for green and yellow letters.
            
            Make sure when inputting a letter that comes up twice, input the green position then remove this index from the duplicate's yellow anti position.
            If left with both occupying the same position, the counts for the letters will not add up and meet requirement, so the list will be incomplete
            
            Press enter.
            """)
            input("""Example Inputs:
            Enter yellow letters: e,y,m
            Enter anti positions: 2345,1234,1345
            Enter green letters: e,r
            Enter positions: 3,4
            
            Press enter to start program
            
            """)

#tkinter window for user inputs if not all overrides given
        window = tkinter.Tk()

        yl_label = tkinter.Label(window, text="Yellow Letters")
        yellow_let_tk = tkinter.Entry()

        ylp_label = tkinter.Label(window, text="Yellow Letter Positions")
        yellow_pos_tk = tkinter.Entry()

        green_label = tkinter.Label(window, text="Green Letters")
        green_tk = tkinter.Entry()

        greenp_label = tkinter.Label(window, text="Green Letter Positions")
        greenp_tk = tkinter.Entry()

        gray_label = tkinter.Label(window, text="Gray Letters")
        gray_tk = tkinter.Entry()

        yl_label.pack()
        yellow_let_tk.pack()

        ylp_label.pack()
        yellow_pos_tk.pack()

        green_label.pack()
        green_tk.pack()

        greenp_label.pack()
        greenp_tk.pack()

        gray_label.pack()
        gray_tk.pack()

        btn_decrease = tkinter.Button(master=window, text="Enter", command=pressedEnter)
        btn_decrease.pack(side=tkinter.BOTTOM, pady=10)
        window.geometry('400x600')
        window.lift()
        window.attributes('-topmost', True)
        window.after_idle(window.attributes, "-topmost", False)
        window.mainloop()


        # yellow_letters_input = input("Enter yellow letters (comma separated): ").lower()
        #
        # yellow_letter_positions_anti_input = input("Enter yellow letter anti positions (comma separated): ").lower()
        #
        # green_letters_input = input("Enter green letters (comma separated): ").lower()
        #
        # green_letter_positions_input = input("Enter green letter positions (comma separated): ").lower()
        #
        # gray_letters_input = input("Enter gray letters (comma separated): ").lower()

#switch to external inputs, if given and CHECK INDIVIDUALLY INSTEAD OF DOING ELSE AND COMBINING WITH ABOVE NONE x 5 AND
    if yellowExternalBypass != None:
        yellow_letters_input = yellowExternalBypass
    if yellowAntiPosExternalBypass != None:
        yellow_letter_positions_anti_input = yellowAntiPosExternalBypass
    if greenExternalBypass != None:
        green_letters_input = greenExternalBypass
    if greenPosExternalBypass != None:
        green_letter_positions_input = greenPosExternalBypass
    if grayExternalBypass != None:
        gray_letters_input = grayExternalBypass

#process inputs into usable data
    if yellow_letters_input != "":
        yellow_letters = list(yellow_letters_input)
        yellow_letters = remove1D(yellow_letters,",")

    else:
        yellow_letters = []

    if yellow_letter_positions_anti_input != "":#the variable names make more sense to me as is, compared to real names. It works, so I am leaving as is for now until testing is
        # #complete, which upon that time, I will change the variable names to traditional variable names instead of names shown
        # #disassemble, subtract 1 from all numbers
        # temp_list = list(yellow_letter_positions_anti_input)
        # indexPointer = 0
        # for letter in temp_list:
        #     try:
        #         temp = int(letter)
        #         temp -= 1
        #         temp_list[indexPointer] = str(temp)#cast back to string after modifications
        #     except:
        #         pass
        #     indexPointer += 1
        # #reassemble input
        # yellow_letter_positions_anti_input_MODIFIED = ""
        # for letter in temp_list:
        #     yellow_letter_positions_anti_input_MODIFIED += letter
        # print(yellow_letter_positions_anti_input_MODIFIED)

        #skip this whole process for improved method; less lines
        yellow_letter_positions_anti_input_MODIFIED = yellow_letter_positions_anti_input
    #NOW continue operations on input as normal, ON MODIFIED DATA, OTHERWISE THE EFFORT AND LENGTHS TAKEN TO MODIFY ARE USELESS IF WE DON'T USE THIS NEW DATA
        list1 = yellow_letter_positions_anti_input_MODIFIED.split(",")
        # print(list1)
        list2 = []
        for entry in list1:
            list2.append(list(entry))
        # print(list2)

        outerIndex = 0
        innerIndex = 0
        for current_list in list2:
            for element in current_list:
                # print(element)
                list2[outerIndex][innerIndex] = int(element) - 1
                innerIndex += 1
            outerIndex += 1
            innerIndex = 0
        # print(list2)
        yellow_letter_positions_anti = list2
    else:
        yellow_letter_positions_anti = []

    if green_letters_input != "":
        green_letters = list(green_letters_input)
        green_letters = remove1D(green_letters,",")

    else:
        green_letters = []

    if green_letter_positions_input != "":
        green_letter_positions = list(green_letter_positions_input)
        green_letter_positions = remove1D(green_letter_positions,",")

        indexPointer = 0
        for element in green_letter_positions:
            green_letter_positions[indexPointer] = int(element) - 1#normalise to 0 index (I then post-applied this strategy to yellow index stuff, to reduce lines by like a dozen or two)
            indexPointer += 1
    else:
        green_letter_positions = []

    if gray_letters_input != "":
        gray_letters = list(gray_letters_input)
        gray_letters = remove1D(gray_letters,",")
        gray_letters = remove1D(gray_letters, " ")#I realised I can now just type the words and because of this, I keep pressing space, as to type normally and put spaces
        #in between ers the words
        for letter in green_letters:#auto remove accidental green letters added to gray input
            gray_letters = remove1D(gray_letters,letter)
        for letter in yellow_letters:#auto remove accidental green letters added to gray input
            gray_letters = remove1D(gray_letters,letter)

        print(gray_letters)
    else:
        gray_letters = []

    # defaultsOrUserInput = input("Use defaults? Default is (N) (Y/N)").lower()
    defaultsOrUserInput = "n"#tkinter window is now up and running

    if defaultsOrUserInput == "y":
        #I could add error checks for null string entries "" but I won't as I am the only one who uses this
        yellow_letters=["e"] #if you have no letters for any of these lists, don't just remove the character, delete the null string entry -> "" (do not just backspace the letters out)
        green_letters=["e","y","m"] #eventually merge with green_letter_positions ??
        gray_letters=["c","n","p","o","l","o"] #confirmed gray letters, from previous guesses (DO NOT STORE DUPLICATES HERE -> if a word has e in it, whether it be yellow or green, do not store the second e - for duplicates - in here)
        green_letter_positions=[0,4,1]#NOTE: uses index 0 as first positon. Standard coding indexing means consistent
        yellow_letter_positions_anti=[[0,1,3,4]]


    aac=[] #stands for all actual combinations
    for word in possible_combos:
        skipFullWord = False #only reset at the start of a new word check
        yellowsPresent = 0
        greensPresent = 0
        letterIndex = 0
        tempYellows = []
        tempGreens = []
        for letter in word:
            if letter not in gray_letters: #only execute if no gray letters, but can be a letter in no list (has not been guessed yet, so has no colour)
                greenMatch = False
                #check if it is a green in the right place
                for greenIndex in range(len(green_letters)):
                    if green_letters[greenIndex] == letter and green_letter_positions[greenIndex] == letterIndex: #if the letter is in green_letters
                        # and the corresponding position pair index matches the current letterIndex, then we should increment
                        greensPresent += 1
                        greenMatch = True

                        #for later (might as well do processing while we got an iterative loop open)
                        tempGreens.append(letter)#letter will be in the correct position because it is green letter


                #otherwise, check if it is present in yellow letter list
                #As positions are not rigid singular positions like green, we don't need to iterate as we did for green. We still need to iterate
                #for next time, use a for loop that checks for all other positions as yellows are yellow because current pos is wrong
                if (not greenMatch) and (letter in yellow_letters): #if letter is in yellow_letters, and we didn't hit a green for the current letter
                    yellow_position_in_yellow_letters = yellow_letters.index(letter)
                    if letterIndex not in yellow_letter_positions_anti[yellow_position_in_yellow_letters]:
                        yellowsPresent += 1
                        yellowMatch = True#not used, but could be, so it is added as to reflect the same functionality as greenMatch green letters can have
                        # if letter not in tempYellows:#commented out to allow for multiple yellow letters of the same letter (lease, giving two e's as yellow. Now, we can track
                        #and validate it as not skipping it, as the count in yellowPresent below after the loop will now no longer skip a valid word)
                        tempYellows.append(letter)#add it. We have to use if statement to weed out duplicates
                    else:
                        skipFullWord = True#I would rather skip the full word, because it's clearly wrong (yellow in the yellow place, duh)

    #this block does not work; it short circuits the word before proper evaluation can be done
            # #yellow cancel save if not at least one of all yellows present in word
            # #note: no reason to green check as if it doesn't meet count then it means not all greens are there. Yellows can have duplicates (Wait, so can greens)
            # if not skipFullWord:#what this basically does is check yellow and green for some reason and it flops because its inside the loop
            #I just realised. Because it says if instead of elif, it runs no matter even if the letter isn't in grey letters. It basically needs to be elif to work. Oops
            #I mean, even then, its useless to have, because if we see a grey we should skipFullWord, which is literally what the else below does, so we only need that to cover all bases
            #     if len(tempYellows) < len(yellow_letters) and len(tempGreens) < len(green_letters):
            #         skipFullWord = True

            else:
                skipFullWord = True#only changed to True once in the word checking, can never be set to False during loop. Will stay True until loop starts again for a new word
                #good implementation of a loop. Invariant stays constant during loop and when it changes, it's change is consistent (no flip-flopping during looping. ...
                # ...Easier to track invariant condition)

            #increm letterIndex tracker (so we can use it for green_letter_positions list
            letterIndex += 1

        #we also check counts as well as if all letters are present (see above for latter -> ctrl+f:"if not skipFullword:")
        if (  greensPresent >= len(green_letters) and yellowsPresent >= len(yellow_letters)  ) and (  not skipFullWord  ):#if the counts match up (old valid logic but missing a check for gray)
            #... and there is not a True skipFullWord signal
            print(greensPresent, yellowsPresent)
            print(word)
            aac.append(word)

        # only checks for exact counts of green and yellow letters
        elif (  greensPresent == len(green_letters) and yellowsPresent == len(yellow_letters)  ) and ( not skipFullWord  ):  # if the counts match up (old valid logic but missing a check for gray)
            # ... and there is not a True skipFullWord signal
            print(greensPresent, yellowsPresent)
            print(word)
            aac.append(word)


    removal = False
    removeWord = []
    for word in aac:
        for letter in yellow_letters:
            if letter not in word:
                removeWord.append(word)
                removal = True

        if not removal:
            for letter in green_letters:
                if letter not in word:
                    removeWord.append(word)

        removal = False


    removeWord = removeDuplicateElements(removeWord)
    for carrier in removeWord:
        print(carrier," removed")
        aac.remove(carrier)


    with open("aac.txt", "w") as f:
        for word in aac:#all actual combinations
            f.write(word + "\n")
            f.close()


    dictionary=enchant.Dict("en_US") #wordle is from the NY times. NY is in the US ∴ en_US dict is used

    for carrier in aac:
        meaning = dictionary.check(carrier)
        if meaning:
            print(carrier,"is a word")
    try:
        # return aac[len(aac)-1]
        return aac
    except:
        with open("aac.txt", "w") as f:
            f.write("no words found" + "\n")
            f.close()
        return "no words found"

if __name__ == '__main__':
    allactualwords = main()#all actual words should really be called all possible words. If the program works correctly,
    #the final word should be present in all sets of guesses from the first guess set of words to the last guess set
    #of words.
    print("All valid words obtained:")
    print(allactualwords)
    print("Guess: " + allactualwords[len(allactualwords)-1])