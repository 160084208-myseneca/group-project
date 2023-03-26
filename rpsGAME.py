import random

# List of valid options
options = ["rock", "paper", "scissors"]

print("Welcome to Rock-Paper-Scissors!")

# Loop for multiple rounds
while True:
    # Computer's random choice
    computer_option = random.choice(options)

    # User input
    user_option = input("Enter your choice (rock/paper/scissors): ").lower()

    # Check if user input is valid
    if user_option not in options:
        print("Invalid choice. Please try again.")
        continue

    # Print user and computer options
    print(f"\nYou chose {user_option}.")
    print(f"The computer chose {computer_option}.\n")

    # Determine winner
    if user_option == computer_option:
        print("It's a tie!")
    elif user_option == "rock":
        if computer_option == "paper":
            print("Computer wins!")
        else:
            print("You win!")
    elif user_option == "paper":
        if computer_option == "scissors":
            print("Computer wins!")
        else:
            print("You win!")
    else:
        if computer_option == "rock":
            print("Computer wins!")
        else:
            print("You win!")

# Ask user to play again
    play_again = input("Do you want to play again? (yes or no): ").lower()
    if play_again == "no":
        break
    
# End of game
print("Thanks for playing!")
