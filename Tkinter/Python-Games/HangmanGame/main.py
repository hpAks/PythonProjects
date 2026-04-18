import csv
import random

from sacremoses.cli import truecase_file

word_list = ["Hangman","Python","Game","Choose","Programming"]
image_list = []

with open("image.txt",mode="r") as file:
    content = file.read()
    content_str = str(content)
    image_list = content_str.split(",")
    #print(f"file content:{str(content_str)}")

def update_show_word(guesses, chosen_word):
    updated_word = ""
    for char in chosen_word:
        if char not in guesses:
            updated_word += "_"
        else:
            updated_word += char
    return updated_word

chosen_word = str(random.choice(word_list)).lower()

#print(f"chosen word: {chosen_word}")
print("Welcome to HangMan game :\n")
play = True
while play:
    guesses = []
    max_attempts = 5
    current_attempt = 0
    show_word = update_show_word("", chosen_word)
    remaining_word = chosen_word
    while current_attempt < max_attempts and len(remaining_word) != 0:
        print(f"Your word : {show_word}")
        # print(f"remaining char to guess: {len(remaining_word)}")
        guess = input("Enter your guess letter: ")
        if guess in guesses:
            print("You already guessed this letter.You lost a turn...")
            current_attempt += 1
            print(image_list[current_attempt])
        else:
            if guess in remaining_word:
                guesses.append(guess.lower())
                remaining_word = remaining_word.replace(guess,"")
                show_word = update_show_word(guesses, chosen_word)
            else:
                print("Wrong guess!\n")
                current_attempt += 1
                print(image_list[current_attempt])


    if len(remaining_word) == 0:
        print(f"You win !! \nChosen word : {chosen_word}")
    else:
        print(f"You lost :( ... \n Chosen word : {chosen_word}")
        print("*************** GAME OVER **********************")
    play = input(f"do you want to continue playing (yes/no):")
    #print(f"selection : {play}")
    if play != "yes":
        break


