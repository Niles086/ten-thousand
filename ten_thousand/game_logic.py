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
        elif all(counts[i] == 1 for i in range(1, 7)):
            score = 1500  # Straight
        elif counts.count(2) == 3:  # Three sets of pairs
            score = 1000  # Pairs
        elif 4 in counts:  # Four-of-a-kind
            score += 200
        elif 5 in counts:  # Five-of-a-kind
            score += 400
        elif 6 in counts:  # Six-of-a-kind
            score += 400

        return score
