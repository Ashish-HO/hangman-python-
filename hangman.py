import random

CHANCES = 5


def find_all(picked_word, character):
    indeces = []
    for index, value in enumerate(picked_word):
        if value == character:
            indeces.append(index)
    return indeces
    pass


# Generate random word
sentence = "It can also be successfully used as a daily exercise to get writers to begin writing. Being shown a random sentence and using it to complete a paragraph each day can be an excellent way to begin any writing session".lower()
words = sentence.split()
picked_word = random.choice(words)
print(picked_word)

#
lst = ["_ "] * len(picked_word)


# interface
print("WELCOME TO HANGMAN GAME.")
print("Word is :")
for _ in lst:
    print("_ ", end="")

# logic
while True:
    indices = []
    guess = input("\nEnter the character:").lower()

    # FOR WORD WISE
    if guess == picked_word:
        print("YOU HAVE GUESSED THE WORD")
        break

    # FOR CHARACTER WISE
    if guess in picked_word:
        indices = find_all(picked_word, guess)
    else:
        print(f"Incorrect.You have got {CHANCES-1} chances.")
        CHANCES = CHANCES - 1

    for i in indices:
        lst.pop(i)
        lst.insert(i, guess)

    for _ in lst:
        print(_ + " ", end=" ")

    if "".join(lst) == picked_word:
        print("\nYou have guessed the word.")
        print(f"The word was {picked_word}.")
        break

    if CHANCES == 0:
        print("\nYOU LOOSE.")
        break
