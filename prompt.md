ai initial prompt

command line version of the dice game Ten Thousand by expanding your understanding of Python standard library
Project named ten-thousand.
Today is all about tackling the highest risk and/or highest priority features - scoring and dice rolling.
Define a GameLogic class in ten_thousand/game_logic.py file.
Handle calculating score for dice roll
Add calculate_score static method to GameLogic class.
The input to calculate_score is a tuple of integers that represent a dice roll.
The output from calculate_score is an integer representing the roll’s score according to rules of game.
Handle rolling dice
Add roll_dice static method to GameLogic class.
The input to roll_dice is an integer between 1 and 6.
The output of roll_dice is a tuple with random values between 1 and 6.
The length of tuple must match the argument given to roll_dice method.

You must document every single line of code with a detailed description of what the code is doing.

10,000 dice game directions 6 Dice Paper for Scoring and pen Dice Tray (optional) Object The player with the highest score above 10,000 points on the final round wins. How to Play Decide who goes first by having everyone roll one die. Whoever has the highest number goes first. Play then continues to the left. The first player rolls all 6 dice. The player can decide to keep as many scoring dice as he/she chooses, but must keep at least one. (See scoring section). Place the scoring dice off to the side and roll the remaining dice. Again the player may keep as many scoring dice as he/she chooses, but must keep at least one. Place scoring dice off the side and roll remaining dice. Play continues until:  Player decides to stop and keep that score OR  Player doesn’t roll any scoring dice and loses score OR  Player has kept all 6 dice. In this case player MUST roll all 6 dice again adding to previous score. Note:  You must earn 800 to start scoring (meaning you can’t stop with 600). Once you reach a score of 800 or more you are “on the board”. Any turn after you are on the board you may keep any score you want (even if it is 100). The Final Round When a player reaches 10,000 (or passes 10,000), every other player gets one more roll. Player with highest score wins. Scoring 1- 100 points 5- 50 points Three of a kind of 1 – 1000 points Three of a kind of 2 – 200 points Three of a kind of 3 – 300 points Three of a kind  of 4 – 400 points Three of a kind of 5 – 500 points Three of a kind of 6 – 600 points For each number over three of a kind you double the amount (example 3 2’s =200, 4 2’s =400, 5 2’s =800, 6 2’s=1,600). Pairs and Straights. When a player rolls 1,2,3,4,5,6 when rolling all 6 dice this is a Straight. When a player gets 3 sets of pairs when rolling 6 dice this is Pairs. Pairs and Straights are worth 1000 points. Note: Three of a kind must all be rolled together. Rolling a 1 and then rolling another 1 and another 1 is 300. Rolling 3 1’s at a time is 1000.  

write the whole program for me and lablle all code samples with the file name for that sample


Int code provided by AI

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
