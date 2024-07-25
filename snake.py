import random

# System randomly chooses Snake (1), Gun (2), or Water (3)
r = int(random.randint(1, 3))

# User input for choice: 1 for Snake, 2 for Gun, 3 for Water
u = int(input("Choose your number 1 for Snake, 2 for Gun, 3 for Water -> "))

# Game logic to determine the winner
if (r == 1 and u == 2):
    print("You won, your gun shoots the snake, system chose Snake and you chose Gun")
elif (r == 2 and u == 1):
    print("System won, system's gun shoots the snake, you chose Snake and system chose Gun")
elif (r == 2 and u == 3):
    print("You won, water rusts the gun, system chose Gun and you chose Water")
elif (r == 3 and u == 2):
    print("System won, water rusts the gun, system chose Water and you chose Gun")
elif (r == 3 and u == 1):
    print("You won, snake drinks water, system chose Water and you chose Snake")
elif (r == 1 and u == 3):
    print("System won, snake drinks water, system chose Snake and you chose Water")
elif (r == u):
    print("Draw!, try again")
else:
    print("Something went wrong!")