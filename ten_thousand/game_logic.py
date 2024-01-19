# ten_thousand/game_logic.py

import random

class GameLogic:
    @staticmethod
    def roll_dice(num_dice):
        return [random.randint(1, 6) for _ in range(num_dice)]

    @staticmethod
    def calculate_score(dice_roll):
        score = 0
        counts = [0] * 7  # Initialize counts for each dice face (1 to 6)

        for dice in dice_roll:
            counts[dice] += 1

        # Calculate score for each dice face
        score += counts[5] // 3 * 500  # Three fives
        score += counts[5] % 3 * 50  # Single fives not part of a three-of-a-kind
        score += counts[1] // 3 * 1000  # Three ones
        score += counts[1] % 3 * 100  # Single ones not part of a three-of-a-kind
        score += counts[2] // 3 * 200  # Three twos
        score += counts[3] // 3 * 300  # Three threes
        score += counts[4] // 3 * 400  # Three fours
        score += counts[6] // 3 * 600  # Three sixes

        # Calculate score for special combinations
        if counts[1] == 6:  # Six ones
            score = 4000
        elif all(counts[i] == 1 for i in range(1, 7)) and not counts[1] == 6:
            score = 1500  # Straight
        elif counts.count(2) == 3:  # Three sets of pairs
            score = 1500  # Three pairs
        elif 4 in counts:  # Four-of-a-kind
            score += 200
        elif 5 in counts:  # Five-of-a-kind
            score += 400
        elif 6 in counts:  # Six-of-a-kind
            score += 400

        return score

    @staticmethod
    def validate_roll(roll, selected_dice):
        """
        Validates the user's roll, checking for cheating or invalid selections.

        Args:
        - roll (list): The current roll of dice.
        - selected_dice (list): The indices of dice selected by the user.

        Returns:
        - bool: True if the roll is valid, False otherwise.
        """
        # Check for cheating or invalid selections
        if len(selected_dice) > len(roll):
            return False

        for index in selected_dice:
            if index < 0 or index >= len(roll):
                return False

        return True

    @staticmethod
    def continue_turn(roll, selected_dice, total_used_dice):
        """
        Continues the turn with the remaining dice after setting aside scoring dice.

        Args:
        - roll (list): The current roll of dice.
        - selected_dice (list): The indices of dice selected by the user.
        - total_used_dice (int): The total number of dice used in the current turn.

        Returns:
        - tuple: A tuple containing the remaining dice and a flag indicating if all dice have been used.
        """
        remaining_dice = [die for i, die in enumerate(roll) if i not in selected_dice]

        # Check if all 6 dice have been used
        all_dice_used = total_used_dice + len(selected_dice) >= 6

        return remaining_dice, all_dice_used

    @staticmethod
    def handle_zilch():
        """
        Handles the case where no points are scored in a round (zilch).

        Returns:
        - int: The score for the round (always 0 for zilch).
        """
        print("Zilch! No points for this round.")
        return 0
