from collections import Counter
import random

WORD_LENGTH = 5


# =========================
# FEEDBACK SIMULATION
# =========================
def get_feedback(guess, secret):
    feedback = ["b"] * WORD_LENGTH
    secret_counts = Counter(secret)

    # greens first
    for i in range(WORD_LENGTH):
        if guess[i] == secret[i]:
            feedback[i] = "g"
            secret_counts[guess[i]] -= 1

    # yellows second
    for i in range(WORD_LENGTH):
        if feedback[i] == "g":
            continue
        if secret_counts[guess[i]] > 0:
            feedback[i] = "y"
            secret_counts[guess[i]] -= 1

    return "".join(feedback)


# =========================
# CHECK IF WORD FITS A GUESS PATTERN
# =========================
def matches(word, guess, feedback):
    wc = Counter(word)

    # FIRST PASS: greens
    for i, ch in enumerate(feedback):
        if ch == "g":
            if word[i] != guess[i]:
                return False
            wc[guess[i]] -= 1

    # SECOND PASS: yellows
    for i, ch in enumerate(feedback):
        if ch == "y":
            if word[i] == guess[i]:
                return False
            if wc[guess[i]] <= 0:
                return False
            wc[guess[i]] -= 1

    # THIRD PASS: greys
    for i, ch in enumerate(feedback):
        if ch == "b":
            # THIS is the key fix:
            # only invalid if we still have unused occurrences left
            if wc[guess[i]] > 0:
                return False

    return True


# =========================
# SOLVER CORE
# =========================
def solve(secret, word_list):
    candidates = word_list[:]

    for step in range(1, 7):
        #print("\n========================")
        #print("STEP", step)

        #print("Possible words:", len(candidates))
        #print("Example:", candidates[:10])

        if not candidates:
            #print("\nNo candidates left (logical error - ran out of words to guess from in word guess pool)")
            return

        # simple heuristic: pick word with most unique letters
        guess = max(candidates, key=lambda w: len(set(w)))

        feedback = get_feedback(guess, secret)

        #print("Guess:", guess)
        #print("Feedback:", feedback)

        if guess == secret:
            #print("\nSOLVED:", secret)
            return 1

        # FILTER USING TRUE WORDLE RULES
        candidates = [
            w for w in candidates
            if matches(w, guess, feedback)
        ]

    #print("\nFailed. Word was:", secret)
    return 0


# =========================
# LOAD WORDS
# =========================
def load_words(path):
    with open(path, "r") as f:
        data = f.readlines()[0].strip(",").split(",")

    return [w.strip().lower() for w in data if len(w.strip()) == 5]


# =========================
# RUN
# =========================
success = 0
times_ran = 100
words = load_words("everywordleword.txt")
for carrier in range(times_ran):
    secret = random.choice(words)
    solve(secret, words)
    success += 1
print(f"Success rate:{success * 100 / times_ran}%")
