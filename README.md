# Sanke-Water-Gun-Game-in-Python
This game also demonstrates the logic of if, else and elif conditional statements
# Snake-Water-Gun Game

## Introduction
The Snake-Water-Gun game is a simple console-based game similar to Rock-Paper-Scissors. Each option (Snake, Water, Gun) can defeat one of the other options based on specific rules.

## Rules
- **Snake vs Water**: Snake drinks water (Snake wins).
- **Water vs Gun**: Water rusts the gun (Water wins).
- **Gun vs Snake**: Gun shoots the snake (Gun wins).

## How to Play
1. The system randomly selects one of the three options (Snake, Water, or Gun).
2. The user is prompted to enter their choice:
   - 1 for Snake
   - 2 for Gun
   - 3 for Water
3. The game compares the choices and determines the winner based on the rules.

## Code Explanation
### Steps
1. **Import the random module**: This is used to generate a random choice for the system.
2. **Generate a random choice for the system**: The system randomly selects between 1 (Snake), 2 (Gun), and 3 (Water).
3. **Prompt the user for input**: The user selects their choice by entering 1, 2, or 3.
4. **Compare choices and determine the winner**:
   - If the system's choice and the user's choice are the same, it's a draw.
   - Specific conditions check who wins based on the game rules.
5. **Print the result**: The result is displayed, indicating whether the user won, the system won, or if it's a draw.

### Note
- If the user's input is invalid or something goes wrong, a message "Something went wrong!" is displayed.
