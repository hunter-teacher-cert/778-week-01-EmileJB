from random import randint

def take_player_turn():
    player_stones_removed = int(input("Enter how many stones you want to remove below (Choose between 1-3): "))
    return player_stones_removed

def take_computer_turn():
    computer_stones_removed = randint(1,3)
    return computer_stones_removed

def display_round_results(computer_stones, stones):
    print(f"The computer removed {computer_stones} stones")
    print(f"There are {stones} stones remaining")

def display_game_winner(winner):
    if winner == "Player":
        print("You Won!")
    elif winner == "Computer":
        print("The Computer Won...")

stones = 12
winner = ""
while stones > 0:
    player_stones_removed = take_player_turn()
    stones = stones - player_stones_removed

    if stones <= 0:
        winner = "Player"

    else:
        computer_stones_removed = take_computer_turn()
        stones = stones - computer_stones_removed

        if stones <= 0:
            winner = "Computer"
            stones = 0

    display_round_results(computer_stones_removed, stones)


display_game_winner(winner)