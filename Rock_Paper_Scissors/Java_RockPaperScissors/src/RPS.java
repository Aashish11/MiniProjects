/**
 * Created: Feb 16, 2021
 * @author: Ashish Singh
 */

import java.util.Scanner;


/**
 * This program calculates the wins, draws, and invalid games
 * between two players of rock, paper, and scissors.
 */
public class RPS
{

	public static void main(String[] args)
	{
		// Declare and initialize variables.
		int totalPlays = 7;
		int invalidGames = 0;
		int p1Wins = 0;
		int p2Wins = 0;
		int draw = 0;
		
		// Default prompt message for the users.
		String userMessage = "please select rock, paper or scissors";
		
		String [] gestures = {"rock", "paper", "scissors"};
		
		// Calls the scanner class
		Scanner userInput = new Scanner(System.in);
		
		// Runs the program seven times and print outs the number of wins of each player,
		// the number of draws, and the invalid gestures entered during the game.
		gameOutcome(userInput, gestures, totalPlays, userMessage, invalidGames, p1Wins, p2Wins, draw);
		
	}
	

	
	/**
	 * Checks if the entries of the users matches to the stored gestures
	 * of rock, paper, and scissors.
	 */
	public static boolean responseMatch(String p1, String[] gestures)
	{
		for (int i = 0; i < gestures.length; i++)
		{
			if (gestures[i].contentEquals(p1))
			{
				return true;
			}
		}
		
		return false;	
	}
	
	
	/**
	 * Calculates the wins, draws, and invalid gestures entered during the game.
	 */
	private static void gameOutcome(Scanner userInput, String[] gestures, int totalPlays
										   , String userMessage, int invalidGames, int p1Wins, int p2Wins
										   , int draw)
	{			
		// Runs the program a total of 7 times and prints out the
		// results at the end of the program.
		for (int i = 0; i < totalPlays; i++)
		{
			System.out.println("Player 1, " + userMessage);
			String p1 = userInput.next();
			
			// If player 1's response doesn't match, 
			// count the invalid game, and start a new game.
			if (responseMatch(p1, gestures) == false)
			{
				invalidGames = invalidGames + 1;
			}
			else
			{
				System.out.println("Player 2, " + userMessage);
				String p2 = userInput.next();
				
				// If player 2's response doesn't match, 
				// count the invalid game, and start a new game.
				if (responseMatch(p2, gestures) == false)
				{
					invalidGames = invalidGames + 1;
				}
				
				// If both players responses are valid, check to see who is
				// the winner.
				else
				{
					if (p1.contentEquals("rock") && p2.contentEquals("paper"))
					{
						p2Wins = p2Wins + 1;
					}
					else if (p2.contentEquals("rock") && p1.contentEquals("paper"))
					{
						p1Wins = p1Wins + 1;
					}
					else if (p1.contentEquals("rock") && p2.contentEquals("scissors"))
					{
						p1Wins = p1Wins + 1;
					}
					else if (p2.contentEquals("rock") && p1.contentEquals("scissors"))
					{
						p2Wins = p2Wins + 1;
					}
					else if (p1.contentEquals("paper") && p2.contentEquals("scissors"))
					{
						p2Wins = p2Wins + 1;
					}
					else if (p2.contentEquals("paper") && p1.contentEquals("scissors"))
					{
						p1Wins = p1Wins + 1;
					}
					else
					{
						draw = draw + 1;
					}
					
				}
				
			}
		
		}
		
		// Prints the result of the game.
		System.out.println("Player 1 won " + p1Wins + " games, "
				 			  + "Player 2 won " + p2Wins + " games, "
				 			  + "and there were " + draw + " ties. "
				 			  + "There were a total of " + invalidGames
				 			  + " invalid games.");
		
	}

}