import random

#  Create an empty list
#  For each letter in the word, replace with "_"

print("WELCOME TO THE HANGMAN GAME!!!")
print("You have 6 guesses to win.")

print()

words = ["farmed", "lamps", "kettle", "people", "matched", "zebras", "yards", "kitty"]
random_word = random.choice(words)
# print(random_word)
display_word  = []
for letter in random_word:
    display_word += "_"
print(display_word)    


print()
#  Ask user to guess a letter
#  Loop through each letter in the random word
#  if guessed letter is ni random_word, replace with "_"

guesses = 0
game_over = False
while not game_over:
    guessed_letter = input("Guess a letter: ")
    for position, letter in enumerate(random_word):
        if letter == guessed_letter:
            display_word[position] = letter

    if guessed_letter not in random_word:
        guesses += 1     
        guesses_left = 5 - guesses

        print(f"You have {guesses_left} guesses left")
        if guesses >= 6:
            print("You ran out of guesses")
            game_over = True   
    print(display_word)      

    if "_" not in display_word:
        print("You Win, Game Over!!!")
        game_over = True
