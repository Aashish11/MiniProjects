"""
Created on Sat Feb 13 2021
@author: Ashish Singh

"""
# Prints a blank line after Python folder path is displayed
# in the terminal.
print()

# Declares a list of options for the game.
# And assigns numeric values to the gestures.
gestures = {"rock": 1, "paper": 2, "scissors": 3}

# Declare and initialize a standard message for players.
user_message = "select rock, paper or scissors: "

# Declare and initialize variables.
p1_wins = 0
p2_wins = 0
p1_invalid_gestures = 0
p2_invalid_gestures = 0
draw = 0

# Executes the rock, paper, and scissors game for 10
# consecutive games.
for i in range(10):
    p1_entry = input("Player 1, " + user_message)
    # Keep asking Player 1 for the gestures until
    # the user enters the proper gesture.
    while (p1_entry not in gestures):
        p1_entry = input("Player 1, " + user_message)
        p1_invalid_gestures = p1_invalid_gestures + 1
    
    p2_entry = input("Player 2, " + user_message)
    # Keep asking Player 2 for the gestures until
    # the user enters the proper gesture.
    while (p2_entry not in gestures):
        p2_entry = input("Player 2, " + user_message)
        p2_invalid_gestures = p2_invalid_gestures + 1

    # The algorithm below assesses whether Player 1 wins,
    # or Player 2 wins, or if it's a draw.
    if ((gestures[p1_entry] - gestures[p2_entry]) % 3 == 2):    # Player 2 wins
        p2_wins = p2_wins + 1
        print()
    elif ((gestures[p1_entry] - gestures[p2_entry]) % 3 == 1):  # Player 1 wins
        p1_wins = p1_wins + 1
        print()
    else:   # Draw
        draw = draw + 1
        print()

# Prints the outcome of the game.
print(f"Player 1 won {p1_wins} games, " \
      f"Player 2 won {p2_wins} games, " \
      f"and there were {draw} ties. " \
      f"Player 1 made {p1_invalid_gestures} invalid gestures " \
      f"and Player 2 made {p1_invalid_gestures} invalid gestures.")