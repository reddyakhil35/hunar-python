import random

def get_computer_choice():
    """Randomly select the computer's choice"""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Compare the choices of user and computer using conditional statements"""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Test your code by playing entering different choices"""
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        user_choice = input("Invalid input. Please enter rock, paper, or scissors: ").lower()
    
    computer_choice = get_computer_choice()
    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")
    
    print(determine_winner(user_choice, computer_choice))

play_game()
