import itertools,string,enchant

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
if len(preloadedCombos) > 0:
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

yellow_letters=["a","t"] #if you have no words, don't just remove the character, delete the null string entry -> "" (do not just backspace the letters out)
green_letters=[] #eventually merge with green_letter_positions ??
gray_letters=["c","r","n","e","y","w","p","s","v","i","l"] #confirmed gray letters, from previous guesses (DO NOT STORE DUPLICATES HERE -> if a word has e in it, whether it be yellow or green, do not store the second e - for duplicates - in here)
green_letter_positions=[3,4]#NOTE: uses index 0 as first positon. Standard coding indexing means consistent
yellow_letter_positions_anti=[[1],[2]]
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
                    yellowMatch = True
                    if letter not in tempYellows:
                        tempYellows.append(letter)#add it. We have to use if statement to weed out duplicates
                else:
                    skipFullWord = True#I would rather skip the full word, because it's clearly wrong (yellow in the yellow place, duh)

        #yellow cancel save if not at least one of all yellows present in word
        #note: no reason to green check as if it doesn't meet count then it means not all greens are there. Yellows can have duplicates (Wait, so can greens)
        if not skipFullWord:
            if len(tempYellows) < len(yellow_letters) and len(tempGreens) < len(green_letters):
                skipFullWord = True

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




with open("aac.txt","w") as f:
    for word in aac:
        f.write(word+"\n")
    f.close()


dictionary=enchant.Dict("en_US") #wordle is from the NY times. NY is in the US ∴ en_US dict is used

for carrier in aac:
    meaning = dictionary.check(carrier)
    if meaning:
        print(carrier,"is a word")