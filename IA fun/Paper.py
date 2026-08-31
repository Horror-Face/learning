import random  # lets us generate random choices, like the computer "thinking"

# a dictionary mapping each choice to the choices it beats
# key = your move, value = list of moves it defeats
beats = {
    "rock": ["scissors"],
    "paper": ["rock"],
    "scissors": ["paper"]
}

choices = list(beats.keys())  # ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

def get_player_choice():
    # keep asking until the player types a valid choice
    while True:
        choice = input(f"Choose {', '.join(choices)}: ").lower().strip()
        if choice in choices:
            return choice
        print("Invalid choice, try again.\n")

print("Welcome to Rock-Paper-Scissors!")
print("First to 3 points wins. Type 'quit' anytime to stop.\n")

while True:  # main game loop, keeps running until someone wins or quits
    player = get_player_choice()

    if player == "quit":
        break  # exits the while loop immediately

    computer = random.choice(choices)  # computer picks randomly from the list
    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a tie!\n")
    elif computer in beats[player]:
        # if the computer's choice is in the list of things "player" beats
        print(f"{player} beats {computer}! You win this round.\n")
        player_score += 1
    else:
        print(f"{computer} beats {player}! Computer wins this round.\n")
        computer_score += 1

    print(f"Score -> You: {player_score} | Computer: {computer_score}\n")

    if player_score == 3:
        print("🎉 You win the game!")
        break  # ends the main loop since the game is over
    elif computer_score == 3:
        print("💻 Computer wins the game!")
        break