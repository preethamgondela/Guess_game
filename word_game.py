"""
File: word_guess.py
-------------------
Fill in this comment.
"""


import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def play_game(secret_word):
    """
    Add your code (remember to delete the "pass" below)
    """
    d=INITIAL_GUESSES
    c=""
    m=0
    for i in range(len(secret_word)): 
            c=c+"-"

    while True:
        print("The word now looks like this "+c)
        print("You have ",d," guesses left.")
        k=input("Type a single letter here, then press enter: ").upper()
        if len(k)!=1:
            print("Guess should only be a single character.")
            continue
        ispres=False
        for i in range(len(secret_word)):
            if secret_word[i]==k:
                #index=secret_word.find(k)
                c=c[:i]+k+c[i+1:]
                ispres=True
        if ispres==False:
            d=d-1
            print("There are no "+k+"'s in the word.")
        if d==0:
            print("Sorry, you lost. The secret word was: "+secret_word)
            return
        if ispres==True:
            print("That guess is correct.")
                #INITIAL_GUESSES=INITIAL_GUESSES-1
        if c==secret_word:
            print("Congratulations, the word is: "+secret_word)
            return
def get_word():
    f = open(LEXICON_FILE)
    words = []

    for line in f:
        words.append(line.strip())

    f.close()

    index = random.randrange(len(words))

    return words[index]


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
