# Hangman Game

import random

# List of words to guess
# words = ["apple", "banana", "cherry", "date", "elderberry"]
words = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
    "ice cream", "jackfruit", "kiwi", "lemon", "mango", "nectarine", "orange",
    "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli fruit",
    "victoria plum", "watermelon", "xigua", "yellow passionfruit", "zucchini",
    "abundance", "bouquet", "cascade", "daffodil", "elegance", "flamenco",
    "giggle", "hazard", "iguana", "jubilee", "kaleidoscope", "luminesce",
    "melody", "narrate", "oceanic", "paprika", "quartz", "reclusive",
    "synchronize", "tactile", "ubiquitous", "vivacious", "wistful", "xenon",
    "yonder", "zestful", "acacia", "brilliant", "calliope", "dynamite",
    "ecstasy", "flirtation", "garrulous", "hypothesis", "insouciant", "jocularity",
    "kibosh", "lissome", "mellifluous", "nemesis", "obfuscate", "parchment",
    "quandary", "rebellious", "sedentary", "tintinnabulation", "ubiquity",
    "venerable", "waxen", "xanthosis", "yoke", "zephyr", "abstruse",
    "bougainvillea", "cathartic", "dichotomy", "euphemism", "fluctuation",
    "garrulity", "heterogeneous", "inscrutable", "jocund", "kaleidoscopic",
    "lachrymose", "mellifluence", "necessity", "obfuscation", "palliative",
    "quixotic", "reclusive", "sediment", "tintinnabulum", "ubiquitousness",
    "venerability", "waxiness", "xanthan", "yonderly", "zestfulness",
    "abstemious", "buxom", "catalyst", "dysania", "euphoria", "florid",
    "garrulousness", "heteronomy", "insouciancy", "jocularity", "kibitzer",
    "lachrymosity", "mellifluousness", "necessarian", "obfuscator", "pallid",
    "quandarian", "reclusiveness", "sedimentation", "tintinnabular",
    "ubiquitousness", "venerableness", "waxenness", "xanthosis", "yonderliness",
    "zestfulness"
]

# Choose a random word from the list
word_to_guess = random.choice(words)

# Create a list to store the guessed letters
guessed_letters = ["_"] * len(word_to_guess)

#Create list of letters tried
tried_letters = []

# Number of lives
lives = 20

print("Welcome to Hangman!")
print('\n',"You have", lives, "lives to guess the word.")

while lives > 0:
    # Print the current state of the word
    print('\n')
    print(" ".join(guessed_letters))

    # Ask the user for a letter
    print('\n')
    letter = input("Guess a letter: ")
    

    # Check if the letter is in the word
    if letter in word_to_guess and letter in guessed_letters:
        print('\n','Already guessed try again.')
    elif letter in word_to_guess:
        # Reveal the correct letter
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == letter:
                guessed_letters[i] = letter
    elif letter in tried_letters and letter not in guessed_letters:
        print('\n','Already guessed try again.')
    else:
        # Decrease the number of lives
        lives -= 1
        tried_letters.append(letter)
        print('\n',"Incorrect! You have", lives, "lives left.")

    # Check if the user has won
    if "_" not in guessed_letters:
        print("Congratulations! You won!", '\n', '\n', 'Your word was', word_to_guess )
        break

if lives == 0:
    print('\n',"Game over! The word was", word_to_guess)