# main.py

from ten_thousand.game_logic import GameLogic
from ten_thousand.utils import get_input

def main():
    print("Welcome to the Ten Thousand dice game!")

    while True:
        # Example usage of roll_dice and calculate_score
        num_dice = get_input("Enter the number of dice to roll: ")
        dice_roll = GameLogic.roll_dice(num_dice)
        print(f"You rolled: {dice_roll}")
        score = GameLogic.calculate_score(dice_roll)
        print(f"Score for this roll: {score}")

        play_again = input("Do you want to roll again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()
