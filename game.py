import random

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Instructions: Choose rock, paper, or scissors. Let's see who wins!\n")

    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Your choice (rock, paper, scissors): ").lower()

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input! Please enter rock, paper, or scissors.")
            continue

        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"Computer chose: {computer_choice}")

        winner = get_winner(user_choice, computer_choice)

        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}\n")

        play_again = input("Play again? (yes/no): ").lower()
        if play_again not in ["yes", "y"]:
            print("\nThanks for playing!")
            print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
            break

if __name__ == "__main__":
    play_game()
