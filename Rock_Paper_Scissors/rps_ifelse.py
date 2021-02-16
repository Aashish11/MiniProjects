"""
Created on Thu Feb 11 2021
@author: Ashish Singh

"""

# Declare and initialize variables.
total_plays = 7
play_count = 0
invalid_games = 0
p1_win = 0
p2_win = 0
draw = 0

# Declare a list of options for the game.
gestures = ["rock", "paper", "scissors"]

# Declare and initialize a standard message for players.
user_message = "select rock, paper or scissors: "

# While loops will continue to execute if the 
# total number of plays is 7. If the total number
# of plays exceed 7, the outcome of the game is 
# displayed to the players.
while (play_count < total_plays):
    print()
    p1_entry = input("Player 1, " + user_message)

    # If player 1 enters a wrong entry, another game
    # is executed, and counts the game played.
    if (p1_entry not in gestures):
        invalid_games = invalid_games + 1
        play_count = play_count + 1
    else:
        p2_entry = input("Player 2, " + user_message)

        # If player 2 enters a wrong entry, another game
        # is executed, and counts the game played.
        if (p2_entry not in gestures):
            invalid_games = invalid_games + 1
            play_count = play_count + 1

        # If correct entries are provided by both users,
        # the following code checks to see who wins; 
        # counts how many wins and draws per players, 
        # and the total number of games played.
        else:
            if (p1_entry == "rock" and p2_entry == "paper"):
                p2_win = p2_win + 1    
            elif (p2_entry == "rock" and p1_entry == "paper"):
                p1_win = p1_win + 1
            elif (p1_entry == "rock" and p2_entry == "scissors"):
                p1_win = p1_win + 1    
            elif (p2_entry == "rock" and p1_entry == "scissors"):
                p2_win = p2_win + 1
            elif (p1_entry == "paper" and p2_entry == "scissors"):
                p2_win = p2_win + 1    
            elif (p2_entry == "paper" and p1_entry == "scissors"):
                p1_win = p1_win + 1
            else:
                draw = draw + 1

            play_count = play_count + 1

# The outcome of the game is only displayed if and only if the total
# number of games played equals 7
print()
print(f"Player 1 won {p1_win} games, " \
        f"Player 2 won {p2_win} games, " \
        f"and there were {draw} ties. " \
        f"There were a total of {invalid_games} " \
        f"invalid games. \n")