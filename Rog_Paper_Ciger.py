import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0
    play_again = True
    
    while play_again:
        print("\nWelcome to Rock, Paper, Scissors!")
        
        # Get user's choice
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        while user_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        
        # Get computer's choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == "rock" and computer_choice == "scissors":
            print("You win! Rock crushes scissors.")
            player_score += 1
        elif user_choice == "paper" and computer_choice == "rock":
            print("You win! Paper covers rock.")
            player_score += 1
        elif user_choice == "scissors" and computer_choice == "paper":
            print("You win! Scissors cut paper.")
            player_score += 1
        elif computer_choice == "rock" and user_choice == "scissors":
            print("You lose! Rock crushes scissors.")
            computer_score += 1
        elif computer_choice == "paper" and user_choice == "rock":
            print("You lose! Paper covers rock.")
            computer_score += 1
        elif computer_choice == "scissors" and user_choice == "paper":
            print("You lose! Scissors cut paper.")
            computer_score += 1
        
        # Display current scores
        print(f"Current Scores - You: {player_score}, Computer: {computer_score}")
        
        # Ask if the player wants to play again
        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        play_again = play_again_input == 'yes'
    
    print("\nThanks for playing Rock, Paper, Scissors!")
    print(f"Final Scores - You: {player_score}, Computer: {computer_score}")

rock_paper_scissors()
