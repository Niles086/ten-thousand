from ten_thousand.game_logic import GameLogic
from ten_thousand.utils import get_input

def main():
    player_name = input("Enter your name: ")
    print(f"Welcome, {player_name}, to the Ten Thousand dice game!")

    total_score = 0
    current_round = 1
    banked_scores = []  # List to store banked scores for each round

    while True:
        print(f"\nRound {current_round}")
        num_dice = get_input("Enter the number of dice to roll: ")
        dice_roll = GameLogic.roll_dice(num_dice)
        print(f"You rolled: {dice_roll}")
        score = GameLogic.calculate_score(dice_roll)
        print(f"Score for this roll: {score}")

        total_score += score
        print(f"Total score: {total_score}")

        play_again = input("Do you want to roll again, bank the current score, or quit? (roll/bank/quit): ").lower()
        if play_again == 'bank':
            banked_scores.append(total_score)  # Add current round's total score to the list
            print(f"Round {current_round} completed. Banking {total_score} points.")
            total_score = 0
            current_round += 1
        elif play_again == 'quit':
            quit_confirmation = input("Are you sure you want to quit? (yes/no): ").lower()
            if quit_confirmation == 'yes':
                break
        elif play_again != 'roll':
            print("Invalid choice. Please enter 'roll', 'bank', or 'quit'.")

    final_total_score = sum(banked_scores)
    print(f"\nGame over, {player_name}! Final total score: {final_total_score}")

if __name__ == "__main__":
    main()
