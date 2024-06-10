import random

#  Create an empty list
#  For each letter in the word, replace with "_"

words = ["farm", "lamp", "kettle", "people", "match", "zebra", "yam", "ok"]
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


game_over = False
while not game_over:
    guessed_letter = input("Guess a letter: ")
    for position, letter in enumerate(random_word):
        if letter == guessed_letter:
            display_word[position] = letter
    print(display_word)      

    if "_" not in display_word:
        print("You Win, Game Over!!!")
        game_over = True
