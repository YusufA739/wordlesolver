import itertools, string
from itertools import count

from attr.validators import max_len

# Define all characters to use in the password
chars = string.ascii_lowercase

# Define MAX_LEN, min_value length and passwordfound
beginningPartial = ""
MAX_LEN = 5
min_value = MAX_LEN - len(beginningPartial)

#list for comparison of values to see what is a word
possible_combos=[]

# Try all possible combinations of characters up to MAX_LEN
for length in range(min_value, min_value + 1):
    for combination in itertools.product(chars, repeat=length):

        # Join the characters in the combination to form a partial word candidate
        candidate = "".join(combination)
        possible_combos.append(str(beginningPartial+candidate))
#generate all possible combos

yellow_letters=[] #if you have no words, don't just remove the character, delete the null string entry -> "" (do not just backspace the letters out)
green_letters=["i","d"]
green_letter_positions=[1,2]
aac=[] #stands for all actual combinations
for word in possible_combos:
    match = False
    yellowsPresent = 0
    greensPresent = 0
    letterIndex = 0
    tempYellows = [] # prevents a letter in yellow and green from making both valid
    tempGreens = []
    for letter in word:
        greenMatch = False
        letterCount = word.count(letter)
        tempYellowsLetterCount = tempYellows.count(letter)
        for greenIndex in range(len(green_letters)):
            if green_letters[greenIndex] == letter and green_letter_positions[greenIndex] == letterIndex: #if the letter is in green_letters
        # and the corresponding position pair index matches the current letterIndex, then we should increment
                greensPresent += 1
                greenMatch = True

        if not greenMatch and letter in yellow_letters and tempYellowsLetterCount < letterCount: #if letter is in yellow_letters, and we haven't reached yellow limit
            yellowsPresent += 1
        letterIndex += 1

    if greensPresent == len(green_letters) and yellowsPresent == len(yellow_letters):
        match = True
    if match:#match has been made redundant but a flag is more descriptive than a long boolean statement, so only for this reason will it not get deleted
        aac.append(word)
print(aac)

file1=open("aac.txt","w")
for carrier in aac:
    file1.write(carrier+"\n")
file1.close()

import enchant
dictionary=enchant.Dict("en_US") #wordle is from the NY times. NY is in the US ∴ en_US dict is used

for carrier in aac:
    meaning = dictionary.check(carrier)
    if meaning:print(carrier,"is a word")