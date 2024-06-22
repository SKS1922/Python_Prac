import random

def guess_the_number():
    best_score = float('inf')
    play_again = True
    
    while play_again:
        actual_number = random.randint(1, 100)
        attempts = 0
        
        print("\nWelcome to the Guessing Game!")
        print("I have picked a random number between 1 and 100. Can you guess it?")
        
        while True:
            try:
                guess = int(input("Enter your guess (between 1 and 100): "))
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                continue

            if not 1<= guess <=100:
                print("Please enter a number between 1 and 100.")
                continue
            
            attempts += 1
            
            if guess < actual_number:
                print("Too low! Try again.")
            elif guess > actual_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {actual_number} correctly in {attempts} attempts!")
                if attempts < best_score:
                    best_score = attempts
                    print(f"🎉 New best score: {best_score} attempts! 🎉")
                break
        
        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        play_again = play_again_input == 'yes'

    print("\nThanks for playing! Your best score was:", best_score)

guess_the_number()