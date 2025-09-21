import random # For random word selection
import csv # For reading words from a CSV file
import os # For clearing the console

# Used ANSI escape codes for colored output in terminals
# Used CSV for word list to allow easy modification and expansion

# Load words from a CSV file
def load_words_from_csv(file):
    valid_words = []
    with open(file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            word = row[0].strip().lower() # words are in the first column
            if len(word) == 5: # Ensure the word is 5 letters long
                valid_words.append(word) # Add to valid words list
    return valid_words, set(valid_words) # Return both List and set , set for O(1) lookups


def check(secret, guess): # Check the guess against the secret word
    status = ["gray"] * 5 # Default status is gray
    secret_chk = [0] * 5 

    for i in range(5):
        if guess[i] == secret[i]:
            status[i] = "green" # Correct letter and position
            secret_chk[i] = 1
    for i in range(5):
        if status[i] == 'gray':
            for j in range(5):
                if guess[i] == secret[j] and secret_chk[j] == 0: # Correct letter, wrong position
                    status[i] = "yellow"
                    secret_chk[j] = 1
                    break
    return status # Return the status list

def display_all_guesses(all_guesses, all_statuses): # Display all guesses with colors
    colors = {"green": "\033[1;42m", "yellow": "\033[1;43m", "gray": "\033[1;100m", "end": "\033[0m"}
    print("\nYour Guesses:")
    print("-------------")
    for guess, status in zip(all_guesses, all_statuses):
        line = ""
        for ch, s in zip(guess, status): # Color each letter based on its status
            line += colors[s] + " " + ch.upper() + " " + colors["end"] + " " # Block style with padding
        print(line.center(40)) # Center the word nicely
    print("-------------\n")

def play_wordle(valid_words, valid_set):
    while True:
        secret = random.choice(valid_words) # Randomly select a secret word
        attempts = 6
        all_guesses = []
        all_statuses = []
        os.system('cls')
        print("\033[1;96m" + "="*40)
        print(" " * 12 + "WORDLE CLI")
        print("="*40 + "\033[0m\n")

        while attempts > 0:
            print(f"\033[1;95mAttempts remaining: {attempts}\033[0m")
            display_all_guesses(all_guesses, all_statuses)

            guess = input("\033[1;97mEnter your guess (5 letters): \033[0m").lower() # Get user input

            if guess == "exit":
                print("\n\033[1;91mThanks for playing!\033[0m")
                return
            if len(guess) != 5 or guess not in valid_set:
                print("\033[1;91mInvalid guess. Please try again.\033[0m\n") # Validate the guess
                continue

            status = check(secret, guess) 
            all_guesses.append(guess)  # Store the guess
            all_statuses.append(status) # Store the status
            os.system('cls') # Clear the console for better readability
            print("\033[1;96m" + "="*40)
            print(" " * 12 + "WORDLE CLI")
            print("="*40 + "\033[0m\n")
            display_all_guesses(all_guesses, all_statuses) # Display all guesses so far

            if status == ["green"] * 5:
                print("\033[1;92mCongratulations! You've guessed the word.\033[0m\n") # Win condition
                break
            attempts -= 1

        if attempts == 0:
            print(f"\033[1;91mSorry, you've run out of attempts. The word was: {secret.upper()}\033[0m\n")
        replay = input("\033[1;93mPlay again? (y/n): \033[0m").lower() # Ask to replay
        if replay != "y":
            print("\n\033[1;94mThanks for playing!\033[0m") # Exit message
            break

if __name__ == "__main__":
    words, words_set = load_words_from_csv("wordle.csv") # Load words from CSV
    play_wordle(words, words_set)  # Start the game
