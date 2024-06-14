import random

# Create a greeting
# Create a word list
# Randomly choose a word from the list created
# Ask the user to guess a letter
# Make a program to take input from the user and make it lowercase
# check if a letter is in a word


print("Creating a word list")
wordList = ["word", "array", "home", "life", "gone"]
print()

print("choosing a random word")
randomWord = random.choice(wordList)
print(randomWord)
print()

guess = input("Guess a letter: ").lower()
print(guess)

for letter in randomWord:
    if letter == guess:
        print("In")
    else:
        print("Out")