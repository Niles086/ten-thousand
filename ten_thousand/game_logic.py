# ten_thousand/game_logic.py

import random

class GameLogic:
    @staticmethod
    def calculate_score(dice_roll):
        """
        Calculate the score for a given dice roll according to the rules of the game.

        Args:
        - dice_roll (tuple): A tuple of integers representing the dice roll.

        Returns:
        - int: The calculated score for the dice roll.
        """
        # Implement scoring rules as per the game instructions
        score = 0
        count = [0] * 7  # Index 0 is not used, indices 1 to 6 represent counts of each number

        for die in dice_roll:
            count[die] += 1

        # Scoring for individual numbers
        score += count[1] * 100  # 1's are worth 100 points each
        score += count[5] * 50   # 5's are worth 50 points each

        # Scoring for three of a kind
        for i in range(1, 7):
            if count[i] >= 3:
                if i == 1:
                    score += 1000  # Three 1's are worth 1000 points
                else:
                    score += i * 100  # Three of any other number are worth 100 times the number

                count[i] -= 3

        # Scoring for additional 1's and 5's
        score += count[1] * 100
        score += count[5] * 50

        # Scoring for pairs and straights
        if all(count[i] > 0 for i in range(1, 7)):
            score += 1000  # Straight

        if any(count[i] >= 2 for i in range(1, 7)):
            score += 1000  # Pairs

        return score

    @staticmethod
    def roll_dice(num_dice):
        """
        Roll a specified number of dice and return the result as a tuple.

        Args:
        - num_dice (int): The number of dice to roll.

        Returns:
        - tuple: A tuple with random values between 1 and 6.
        """
        # Roll the specified number of dice and return the result as a tuple
        return tuple(random.randint(1, 6) for _ in range(num_dice))
