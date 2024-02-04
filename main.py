from ten_thousand.game_logic import GameLogic
from ten_thousand.utils import get_input

def main():
    player_name = input("Enter your name: ")
    print("Welcome, {}, to the Ten Thousand".format(player_name))

    total_score = 0
    current_round = 1
    banked_scores = []  # List to store banked scores for each round

    while current_round <= 10 and total_score < 800:
        print("\nRound {}".format(current_round))
        remaining_dice = 6  # Move this line inside the loop

        while remaining_dice > 0:
            try:
                num_dice = int(input("Enter the number of dice to roll: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            dice_roll = GameLogic.roll_dice(num_dice)
            print("You rolled: {}".format(dice_roll))
            score = GameLogic.calculate_score(dice_roll)

            if score == 0:
                print("Zilch! No points for this roll.")
                total_score += GameLogic.handle_zilch()
                break
            else:
                print("Score for this roll: {}".format(score))
                print("Total score: {}".format(total_score + score))

            remaining_dice -= num_dice

            if remaining_dice == 0:
                print("All dice used for this turn.")
                break

            play_again = input("Do you want to roll again, bank the current score, or quit? (roll/bank/quit): ").lower()
            if play_again == 'bank':
                banked_scores.append(total_score + score)
                print("Round {} completed. Banking {} points.".format(current_round, total_score + score))
                total_score = 0
                break
            elif play_again == 'quit':
                quit_confirmation = input("Are you sure you want to quit? (yes/no): ").lower()
                if quit_confirmation == 'yes':
                    current_round = 11  # Exit the game loop
                    break
            elif play_again != 'roll':
                print("Invalid choice. Please enter 'roll', 'bank', or 'quit'.")

        current_round += 1

    final_total_score = sum(banked_scores)
    print("\nGame over, {}! Final total score: {}".format(player_name, final_total_score))

if __name__ == "__main__":
    main()
