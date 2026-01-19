import itertools, string, enchant
words= []
dictionary=enchant.Dict("en_US") #wordle is from the NY times. NY is in the US ∴ en_US dict is used

for combination in itertools.product(string.ascii_lowercase,repeat=5):
    word = "".join(combination)
    if dictionary.check(word):
        words.append(word)
with open("wordlegen.txt","w") as f:
    for carrier in words:
        f.write(carrier+"\n")
    f.close()