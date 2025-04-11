import random

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Word bank of animals
word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

# Randomly choose a word from the word_list
chosen_word = random.choice(word_list)
# print(f"Chosen word (for testing): {chosen_word}")  # You may remove this after testing.

# Create a placeholder list to display the word as underscores
word_length = len(chosen_word)
display = ["_"] * word_length  # Use a list for easier modification.

# Game variables
game_over = False
number_of_lives = 6  # Matches the number of Hangman stages
guessed_letters = set()  # Set to track guessed letters

print(" ".join(display))

while not game_over:
    guess = input("Guess a letter: ").lower()

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try a different letter.")
        continue

    guessed_letters.add(guess)  # Store guessed letter

    correct_guess = False  # Reset for each round

    # Check if the guessed letter is in the word
    for index in range(word_length):
        if chosen_word[index] == guess:
            display[index] = guess
            correct_guess = True

    if correct_guess:
        print("Right")
    else:
        number_of_lives -= 1  # Decrease life only if the guess is incorrect
        print("Wrong")
        print("You lose a life")
        print(f"{number_of_lives} lives left")

    # Print the current stage of Hangman
    print(stages[6 - number_of_lives])

    # Print the updated word display
    print(" ".join(display))

    # Show guessed letters
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

    # Check if the player has guessed all letters
    if "_" not in display:
        game_over = True
        print("You win!")

    # Check if the player has run out of lives
    if number_of_lives <= 0:
        game_over = True
        print("You lose!")
        print(f"The word was: {chosen_word}")
