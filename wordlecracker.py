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

yellow_letters=["c","a"] #if you have no words, don't just remove the character, delete the null string entry -> "" (do not just backspace the letters out)
green_letters=[]
gray_letters=["r","n","e"] #confirmed gray letters, from previous guesses (DO NOT STORE DUPLICATES HERE -> if a word has e in it, whether it be yellow or green, do not store the second e - for duplicates - in here)
green_letter_positions=[]#NOTE: uses index 0 as first positon. Standard coding indexing means consistent
aac=[] #stands for all actual combinations
for word in possible_combos:
    match = False
    yellowsPresent = 0
    greensPresent = 0
    letterIndex = 0
    tempYellows = [] # prevents a letter in yellow and green from making both valid
    tempGreens = []
    for letter in word:
        if letter in gray_letters: #immediately stop. This word will not be the one (contains a known gray, which means it cannot be word, grays are wrong)
            break
        greenMatch = False
        letterCount = word.count(letter)
        tempYellowsLetterCount = tempYellows.count(letter)
        for greenIndex in range(len(green_letters)):
            if green_letters[greenIndex] == letter and green_letter_positions[greenIndex] == letterIndex: #if the letter is in green_letters
                # and the corresponding position pair index matches the current letterIndex, then we should increment
                greensPresent += 1
                greenMatch = True

        if (not greenMatch) and (letter in yellow_letters) and (tempYellowsLetterCount < letterCount): #if letter is in yellow_letters, and we haven't reached yellow limit
            yellowsPresent += 1
        letterIndex += 1

    if greensPresent == len(green_letters) and yellowsPresent == len(yellow_letters):
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