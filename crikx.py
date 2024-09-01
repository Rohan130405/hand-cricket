import random

def get_valid_input(options):
    while True:
        player_choice = input("Enter your number (0, 1, 2, 3, 4, 6): ")
        if player_choice.isdigit():
            player_choice = int(player_choice)
            if player_choice in options:
                return player_choice
        print("Invalid input. Please enter a valid number (0, 1, 2, 3, 4, 6).")

def play_innings(player_type, options, target=None):
    score = 0
    while True:
        player_choice = get_valid_input(options)
        comp_choice = int(random.choice(options))
        print(f"Computer chose: {comp_choice}")

        if player_choice == comp_choice:
            print(f"**** {player_type} is out at {score} ****")
            break
        else:
            score += player_choice if player_type == "You" else comp_choice
            print(f"Score: {score}")

            if target is not None and score > target:
                print(f"{player_type} surpasses the target with a score of {score}!")
                break
    return score

def declare_winner(user_score, comp_score):
    if user_score > comp_score:
        print("**** You won the match! ****")
    elif user_score < comp_score:
        print("**** Computer won the match! ****")
    else:
        print("**** Match Tied! ****")

def hand_cricket():
    toss_options = ['head', 'tails']
    game_options = [0, 1, 2, 3, 4, 6]

    user_toss = input("Enter your choice (heads or tails): ").lower()
    print(f"You chose: {user_toss}")
    original_toss = random.choice(toss_options)
    print(f"Toss result: {original_toss}")

    if user_toss == original_toss:
        print("You won the toss!")
        user_choice = input("Choose to bat or ball: ").lower()
        if user_choice == 'bat':
            user_score = play_innings("You", game_options)
            print(f"Target for the computer is {user_score + 1}")
            comp_score = play_innings("Computer", game_options, target=user_score)
        else:
            comp_score = play_innings("Computer", game_options)
            print(f"Target for you is {comp_score + 1}")
            user_score = play_innings("You", game_options, target=comp_score)
    else:
        print("You lost the toss.")
        comp_choice = random.choice(['bat', 'ball'])
        print(f"Computer chose to {comp_choice}.")
        if comp_choice == 'bat':
            comp_score = play_innings("Computer", game_options)
            print(f"Target for you is {comp_score + 1}")
            user_score = play_innings("You", game_options, target=comp_score)
        else:
            user_score = play_innings("You", game_options)
            print(f"Target for the computer is {user_score + 1}")
            comp_score = play_innings("Computer", game_options, target=user_score)

    declare_winner(user_score, comp_score)

hand_cricket()
