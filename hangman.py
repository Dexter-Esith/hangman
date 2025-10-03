import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6  # total lives
print(logo)  # print the hangman logo

chosen_word = random.choice(word_list).lower()  # randomly pick a word and make it lowercase
word_length = len(chosen_word)

display = "_" * word_length  # placeholder for the word to guess
print("Word to guess: " + display)

game_over = False
correct_letters = []  # list to store correct guessed letters
wrong_letters = []    # list to store wrong guessed letters

while not game_over:
    print(f"\n************* {lives}/6 LIVES LEFT *************")
    guess = input("Guess a letter: ").lower().strip()  # ask player for a letter

    # validate input: must be a single alphabetic character
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter (a-z).")
        continue  # skip to next loop without losing a life

    # already guessed correctly
    if guess in correct_letters:
        print(f"You've already guessed '{guess}' (correct).")
        print("Word to guess: " + display)
        print(stages[lives])
        continue

    # already guessed incorrectly
    if guess in wrong_letters:
        print(f"You've already guessed '{guess}' (wrong).")
        print("Word to guess: " + display)
        print(stages[lives])
        continue

    # check if guess is in the chosen word
    if guess in chosen_word:
        correct_letters.append(guess)  # add to correct list once
    else:
        wrong_letters.append(guess)  # add to wrong list once
        lives -= 1  # lose a life for wrong guess
        print(f"'{guess}' is not in the word. You lose a life.")

    # rebuild display string based on correct letters
    display = "".join(letter if letter in correct_letters else "_" for letter in chosen_word)
    print("Word to guess: " + display)

    # check win condition
    if "_" not in display:
        game_over = True
        print("******************** YOU WIN ********************")

    # check lose condition
    if lives <= 0:
        game_over = True
        print(f"******** IT WAS '{chosen_word.upper()}' — YOU LOSE ********")

    # print the hangman stage corresponding to remaining lives
    print(stages[lives])
