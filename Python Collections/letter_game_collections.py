import os
import random
import sys

with open("letter_game.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
WORDS = [x.strip() for x in content]


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def draw(bad_guesses, good_guesses, secret_word):
    clear()
    print('Strikes: {}/7'.format(len(bad_guesses)))
    print('\n')

    print("Missed letters:", end=' ')
    for letter in bad_guesses:
        print(letter, end=' ')
    print('\n\n')

    for letter in secret_word:
        if letter in good_guesses:
            print(letter, end=' ')
        else:
            print('_', end=' ')

    print('\n\n')


def get_guess(guesses):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("You can only guess a single letter!")
        elif guess in guesses:
            print("You've already guesses that letter!")
        elif not guess.isalpha():
            print("You can only guess letters!")
        else:
            return guess


def play(done):
    clear()
    secret_word = random.choice(WORDS).lower()
    bad_guesses = set()
    good_guesses = set()
    secret_word_set = set(secret_word)

    while True:
        draw(bad_guesses, good_guesses, secret_word)
        guess = get_guess(bad_guesses | good_guesses)

        if guess in secret_word_set:
            good_guesses.add(guess)
            if not secret_word_set.symmetric_difference(good_guesses):
                print("You win!")
                print("The secret word was {}".format(secret_word))
                done = True
        else:
            bad_guesses.add(guess)
            if len(bad_guesses) == 7:
                draw(bad_guesses, good_guesses, secret_word)
                print("You lost!")
                print("The secret word was {}".format(secret_word))
                done = True

        if done:
            play_again = input("Play again? Y/n ").lower()
            if play_again != 'n':
                return play(done=False)
            else:
                sys.exit()


def welcome():
    start = input("Press enter/return to start or Q to quit ").lower()
    if start == 'q':
        print("Bye!")
        sys.exit()
    else:
        return True


print("Welcome to Letter Guess!")

done = False

while True:
    clear()
    welcome()
    play(done=done)
