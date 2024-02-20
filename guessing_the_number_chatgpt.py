import random

def guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    while True:
        play_game()
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing!")

def play_game():
    pc_number = random.randint(1, 10)
    attempts = 0
    min_attempts = float('inf')
    
    print("I'm thinking of a number between 1 and 10...")
    
    while True:
        player_number = get_player_input()
        attempts += 1
        
        if player_number == pc_number:
            print(f"Congratulations! You guessed the number {pc_number} correctly!")
            min_attempts = min(min_attempts, attempts)
            break
        elif player_number < pc_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")
    
    print(f"You guessed it in {attempts} attempts.")
    print(f"The minimum number of attempts so far is: {min_attempts}")

def get_player_input():
    while True:
        player_number = input("Can you guess the number? Enter your guess: ")
        if not player_number.isdigit() or not 1 <= int(player_number) <= 10:
            print("Please enter a valid number between 1 and 10.")
            continue
        return int(player_number)

# Start the game
guessing_game()
