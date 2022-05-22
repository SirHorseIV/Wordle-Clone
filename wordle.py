from random import randint
import os


def getWords(filename):
    words = []
    with open(filename, "r") as file:
        for word in file:
            words.append(word[:-1])
    return words


def occurences(word):
    letterOcc = {}
    for letter in word:
        if not letter in letterOcc:
            letterOcc[letter] = 1
        else:
            letterOcc[letter] += 1
    return letterOcc


def guess(word, answer, letterPrev):
    letterOcc = occurences(answer)
    word = list(word)
    output = [None]*5
    for i in range(len(word)):
        if word[i] == answer[i]:
            output[i] = "\033[4;48;2;4;130;56m" + " "  + word[i] + " "  + "\033[0m"
            letterOcc[word[i]] -= 1
            letterPrev[word[i]] = "\033[38;2;13;188;121m" + word[i] + "\033[0m"
            word[i] = "X"
    for i in range(len(word)):
        if word[i] in answer:
            if letterOcc[word[i]] > 0:
                letterOcc[word[i]] -= 1
                output[i] = "\033[4;48;2;180;120;4m" + " "  + word[i] + " "  + "\033[0m"
                if letterPrev[word[i]] == word[i]:
                    letterPrev[word[i]] = "\033[38;2;200;160;9m" + word[i] + "\033[0m"
            else:
                output[i] = "\033[4;48;2;102;102;102m" + " " + word[i] + " "  + "\033[0m"
        elif word[i] != "X":
            output[i] = "\033[4;48;2;102;102;102m" + " "  + word[i] + " "  + "\033[0m"
            if word[i] in letterPrev:
                if letterPrev[word[i]] == word[i]:
                        letterPrev.pop(word[i])
    return " ".join(output)


def getAnswer(words, start, end):
    return words[randint(start, end)]


os.system("")
length = 5
words = getWords("words.txt")
selecting = True
while selecting:
    print("Easy, Normal, Hard, or Impossible?")
    inp = input().lower()
    if inp == "easy" or inp == "e" or inp == "1":
        numOfGuesses = 7
        wordRange = [0, 500]
    elif inp == "normal" or inp == "n" or inp == "2":
        numOfGuesses = 6
        wordRange = [500, 1500]
    elif inp == "hard" or inp == "h" or inp == "3":
        numOfGuesses = 5
        wordRange = [1500, 2000]
    elif inp == "impossible" or inp == "i" or inp == "4":
        numOfGuesses = 5
        wordRange = [5000, 5500]
    else:
        print("Invalid input")
        continue
    selecting = False
answer = getAnswer(words, wordRange[0], wordRange[1])
guessNum = 0
guesses = [" ".join(["\033[4;48;2;102;102;102m   \033[0m"]*length)]*numOfGuesses
letterPrev = {"a": "a", "b": "b", "c": "c", "d": "d", "e": "e", "f": "f", "g": "g", "h": "h", "i": "i", "j": "j", "h": "h",
              "k": "k", "l": "l", "m": "m", "n": "n", "o": "o", "p": "p", "q": "q", "r": "r", "s": "s", "t": "t", "u": "u",
              "v": "v", "w": "w", "x": "x", "y": "y", "z": "z"}
won = False
while guessNum < numOfGuesses:
    print(" ".join(letterPrev.values()))
    inp = input("Guess a five letter word: ").lower()
    if len(inp) != 5 or not inp.isalpha():
        print("Word must be five letters long, and must only include letters")
    elif not inp in words:
        print("Word not found in dictionary")
    else:
        guesses[guessNum] = guess(inp, answer, letterPrev)
        print("\n".join(guesses))
        guessNum+=1
        if inp == answer:
            won = True
            break
if won:
    print("Well done, you got the word in", str(guessNum) +"!")
else:
    print("You've ran out of guesses\nThe word was", answer)
input()
