import random

# Constants for game choices
SNAKE = 1
WATER = -1
GUN = 0

# Mapping dictionaries
CHOICE_TO_SYMBOL = {'s': SNAKE, 'w': WATER, 'g': GUN}
SYMBOL_TO_NAME = {SNAKE: "Snake", WATER: "Water", GUN: "Gun"}

# Game rules - what beats what
GAME_RULES = {
    (SNAKE, WATER): True,    # Snake beats Water
    (WATER, GUN): True,      # Water beats Gun
    (GUN, SNAKE): True,      # Gun beats Snake
}

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a draw"
    elif (player_choice, computer_choice) in GAME_RULES:
        return "You win!"
    else:
        return "You lose!"

# Game execution
computer_choice = random.choice([SNAKE, WATER, GUN])
user_input = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

try:
    player_choice = CHOICE_TO_SYMBOL[user_input]
    
    print(f"\nYou chose {SYMBOL_TO_NAME[player_choice]}")
    print(f"Computer chose {SYMBOL_TO_NAME[computer_choice]}")
    
    result = determine_winner(player_choice, computer_choice)
    print(result)

except KeyError:
    print("Invalid input! Please enter 's', 'w', or 'g'.")