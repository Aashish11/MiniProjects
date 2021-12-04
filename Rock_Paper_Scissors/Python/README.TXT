



Approach: 
--> For the first part (rps_ifelse.py), I created a list with the game's gestures, i.e., rock, paper, and scissors. 
I then took a tiered approach to decide the winner of the game. Even though the number of iteration (7) is known, 
I used a "while" loop to loop the program seven times and used a counter to exit the loop once the counter reached 7.

Certain conditions had to be met in the program:
a) If player 1 enters a wrong response that is not in the list, start another game.
b) If player 1's response is valid, but player 2 enters a wrong response that is not in the list, start another game.
c) Only when both the responses from player 1 and player 2 are valid, calculate the wins and draw between the users.

Hence, at the beginning of the program, the algorithm searches if player 1's response is valid. 
If player 1's response is not valid, the program requests player 1 to re-enter the response. 
Only when player 1's response is valid, the program asks player 2 for input. 
If player 2's response is not valid, the program starts another game by asking player 1 for input. 
If the users enter any mistake in their response, such as a spelling error, another game is started.

If both the users enter a valid gesture, the if/elif/else statement checks to see which of the users' responses is a winner. 
There is one if statement, five elif statements, and one else statement. 
The reason for selecting this option versus multiple if statements are that we only need one statement to be true, and we do not require to check all of the other options.

The else statement is configured in such a way that only the response "paper", "paper", or "rock", "rock", or "scissors", "scissors" is captured in the else statement, which qualifies for a draw.

At the end of the game, a printout is displayed to the user, showing both the users' wins, draws, and invalid gestures entered in the program.

--> For the second part (rps_modular.py), I used a set to store the gestures and their numerical representation. 
Scissors trumps paper, and paper trumps rock. Hence, I assigned 1 to rock, 2 to paper, and  3 to scissors.

Unlike the rps_ifelse.py with the if/elif/else statement, using modulo arithmetic to decide a winner condensed the program. 
In addition to the modulo arithmetic, I used a "for" loop in this program because it needed to run ten times. 
The loop in the program can be run using a while loop similar to the first program. 
However, I wanted to demonstrate the program's desired outcome can be obtained by both a "while" loop and a "for" loop.

The conditions for the second part of the assignment were different and had to be adjusted accordingly:
a) Keep asking player 1 for a valid response until a valid response is given and count the invalid gestures entered by player 1.
b) Keep asking player 2 for a valid response until a valid response is provided and count the invalid gestures entered by player 2.
c) Calculate the wins and draw between the players.

There are two separate "while" loops in the program. 
If I used an if/else statement for players' response instead of the "while" loop, at most, I could have given the user two tries to enter a valid response. 
However, with a "while" loop, the prospective prompt for a valid response is infinite. 

For calculating the winner, I tried different operations to formulate an equation. 
I needed a different outcome when the users selected "rock", "paper" vs. "paper", "rock", and when there was a draw. 
So, dividing one number by another number was not sufficient. 
Adding the numeric representation of the user's entries and then calculating a remainder would not have worked either, as the outcome would have been the same.
Hence, I subtracted one user's response from another user's response and took the remainder, producing the desired outcome.

In conclusion, once the construct of the loops and if/elif/else statements are fully understood, the programmer can use any of those options to get the desired result.

Known Bug: 
NA