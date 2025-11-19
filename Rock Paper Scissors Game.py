# Rock, Paper, Scissors game in Python
# Author: Simon Mulligan
# This program allows a user to play Rock, Paper, Scissors against the computer.
# The computer's choice is generated randomly using the random module.
# Scores are tracked until the user decides to stop playing.

import random

def play_game():
    # Initialize scores
    player_score = 0
    computer_score = 0

    # Define possible choices
    choices = ['r', 'p', 's']  # r = Rock, p = Paper, s = Scissors

    while True:
        # Ask the user for their choice
        user_choice = input("Enter a choice (Rock(r), Paper(p), Scissors(s)): ").lower()

        # Validate input
        if user_choice not in choices:
            print("Invalid choice! Please enter r, p, or s.")
            continue

        # Computer randomly selects a choice
        computer_choice = random.choice(choices)

        # Map short form to full word for display
        choice_map = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
        print(f"\nYou chose {choice_map[user_choice]}, the computer chose {choice_map[computer_choice]}.")

        # Determine the winner
        if user_choice == computer_choice:
            print(f"Both players selected {choice_map[user_choice]}. It's a tie!\n")
        elif user_choice == 'r':
            if computer_choice == 's':
                print("Rock smashes Scissors! You win!\n")
                player_score += 1
            else:
                print("Paper covers Rock! You lose.\n")
                computer_score += 1
        elif user_choice == 'p':
            if computer_choice == 'r':
                print("Paper covers Rock! You win!\n")
                player_score += 1
            else:
                print("Scissors cut Paper! You lose.\n")
                computer_score += 1
        elif user_choice == 's':
            if computer_choice == 'p':
                print("Scissors cut Paper! You win!\n")
                player_score += 1
            else:
                print("Rock smashes Scissors! You lose.\n")
                computer_score += 1

        # Ask if the user wants to play again
        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            break

    # Print final scores
    print("\nFinal Scores:")
    print("Computer:", computer_score)
    print("Player:", player_score)

# Run the game
play_game()
