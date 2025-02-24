import random

# ASCII Art for the choices
choices_art = {
    "rock": '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    ''',
    "paper": '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    ''',
    "scissors": '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
}

# Choices list
choices = ["rock", "paper", "scissors"]


def get_user_choice():
    try:
        user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
        if user_input not in [0, 1, 2]:
            raise ValueError
        return user_input
    except ValueError:
        print("Invalid choice. Please enter 0, 1, or 2.")
        exit()


def get_computer_choice():
    return random.randint(0, 2)


def determine_winner(user, computer):
    if user == computer:
        return "It's a draw!"
    elif ((user == 0 and computer == 2) or
          (user == 1 and computer == 0) or
          (user == 2 and computer == 1)):
        return "You win!"
    else:
        return "You lose!"


print("Welcome to Rock, Paper, Scissors!")

user_choice = get_user_choice()
computer_choice = get_computer_choice()

user_choice_text = choices[user_choice]
computer_choice_text = choices[computer_choice]

print(f"\nYou chose:\n{choices_art[user_choice_text]}")
print(f"Computer chose:\n{choices_art[computer_choice_text]}")

print(determine_winner(user_choice, computer_choice))