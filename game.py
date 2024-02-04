from ten_thousand.game_logic import GameLogic
from ten_thousand.utils import get_input

def main():
    player_name = input("Enter your name: ")
    print("Welcome, {}, to the Ten Thousand".format(player_name))

    start_game = input("(y)es to play or (n)o to decline\n> ").lower()
    if start_game != 'y':
        print("Maybe next time. Goodbye!")
        return

    total_score = 0
    current_round = 1
    banked_scores = []  # List to store banked scores for each round

    while current_round <= 10 and total_score < 800:
        print("\nStarting round {}".format(current_round))
        print("Rolling 6 dice...")
        dice_roll = GameLogic.roll_dice(6)
        print("*** {} ***".format(' '.join(map(str, dice_roll))))

        while True:
            keep_dice = input("Enter dice to keep, or (q)uit:\n> ")
            if keep_dice.lower() == 'q':
                print("Thanks for playing. You earned {} points".format(total_score))
                return

            try:
                kept_values = [int(d) for d in keep_dice]
            except ValueError:
                print("Invalid input. Please enter valid dice values.")
                continue

            remaining_dice = 6 - len(kept_values)
            score = GameLogic.calculate_score(kept_values)

            if score == 0:
                print("Zilch! No points for this roll.")
                total_score += GameLogic.handle_zilch()
                break
            else:
                print("You have {} unbanked points and {} dice remaining".format(total_score + score, remaining_dice))
                action = input("(r)oll again, (b)ank your points or (q)uit:\n> ").lower()

                if action == 'b':
                    banked_scores.append(total_score + score)
                    print("You banked {} points in round {}".format(total_score + score, current_round))
                    total_score = 0
                    break
                elif action == 'q':
                    print("Thanks for playing. You earned {} points".format(total_score + score))
                    return
                elif action != 'r':
                    print("Invalid choice. Please enter 'r', 'b', or 'q'.")
                    continue

        current_round += 1

    final_total_score = sum(banked_scores)
    print("\nGame over, {}! Final total score: {}".format(player_name, final_total_score))

if __name__ == "__main__":
    main()
