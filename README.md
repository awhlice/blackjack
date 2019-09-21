# Blackjack
A console-based interactive game of Blackjack

# Instructions for running code
1) Open the command line
2) Type the below commands in succession:
    - git clone https://github.com/awhlice/blackjack.git
    - cd blackjack
    - python ./blackjack.py
3) Enjoy the game!
    - For further clarification: Type ‘H’, ‘S’, or ‘Q’ into the command line when prompted to execute your desired action

# Sample test runs

### First test run

Let's play Blackjack!  
\------------------------------------------------------------------------------------\-  
You are holding the 9 of Clubs and 1 of Spades for a total of 10 points.  
The dealer is showing the 10 of Clubs.  

Would you like to [H]it, [S]tand, or [Q]uit? H  
You received a 4 of Hearts. You now have a total of 14 points.  

Would you like to [H]it, [S]tand, or [Q]uit? W  
Sorry, you can't perform that action.  

Would you like to [H]it, [S]tand, or [Q]uit? S  

The dealer revealed their face-down card to be the King of Hearts.  

To recap, you are holding the 9 of Clubs, 1 of Spades and 4 of Hearts for a total of 14 points.  
The dealer is holding the 10 of Clubs and King of Hearts for a total of 20 points.  

Sorry, you lose! The dealer's hand is closer to 21.  
\------------------------------------------------------------------------------------\-  
Exiting Blackjack...  

### Second test run

Let's play Blackjack!  
\------------------------------------------------------------------------------------\-  
You are holding the 8 of Clubs and 3 of Spades for a total of 11 points.  
The dealer is showing the 3 of Hearts.  

Would you like to [H]it, [S]tand, or [Q]uit? H  
You received a 5 of Spades. You now have a total of 16 points.  

Would you like to [H]it, [S]tand, or [Q]uit? H  
You received a 6 of Spades. You now have a total of 22 points.  

Sorry, you lose! You busted.  
\------------------------------------------------------------------------------------\-  
Exiting Blackjack...  

### Third test run

Let's play Blackjack!  
\------------------------------------------------------------------------------------\-  
You are holding the 5 of Clubs and 9 of Clubs for a total of 14 points.  
The dealer is showing the 4 of Clubs.  

Would you like to [H]it, [S]tand, or [Q]uit? H  
You received a 7 of Spades. You now have a total of 21 points.  

Would you like to [H]it, [S]tand, or [Q]uit? S  

The dealer revealed their face-down card to be the 9 of Hearts.  
The dealer took the Jack of Spades.  

To recap, you are holding the 5 of Clubs, 9 of Clubs and 7 of Spades for a total of 21 points.  
The dealer is holding the 4 of Clubs, 9 of Hearts and Jack of Spades for a total of 23 points.  

Congratulations, you got Blackjack!  
\------------------------------------------------------------------------------------\-  
Exiting Blackjack...  

# Game rules
- Standard rules for a game of Blackjack
    - Omitted the double down and split options for the player in order to finish under 3 hours (the game does not implement the option to place bets)

# Explanation of design choices
The program is centered on the Player, Card, and Deck class, since I knew that these objects, once created, would be passed around frequently in my code. The attributes of each class are intuitive: The Card class contains the value and suit of the card at hand, while the Player class contains the player’s current hand as well as a function that calculates the amount of points they possess based on their hand. The Deck class is essentially an array of Card objects, but I included an initialization function within the class, so that it would be ready to use as soon as it was instantiated.

I represented each hand and deck of cards as an array of Card objects, because the pre-existing pop() and append() functions provided by python can be called to take cards from the deck and add them onto the player’s hand. In addition, I created various functions to represent the different actions (hit(), stand(), and quit()) and stages (begin(), outcome()) of a game of Blackjack. To sum it up, I created the three classes and separate functions to improve the readability of my code and mimic the individual components of a game of Blackjack.

# Choice of tooling
I used python 2.7.10, because of its flexibility and readability. Since it provides many pre-existing functions (such as the pop() and shuffle() functions I mentioned prior), it was easier to focus on how I wanted to structure, rather than implement, my program; Once I had a solid idea of its composition, I could smoothly translate my idea into python. I could better abstract my code through the use of classes as well, because python supports object-oriented design.

Gameplay felt too rushed when lines were  printed in succession, so I slowed it down by importing the system/time modules to aid in creating the effect of typing on the terminal. I imported the random module, so I could call shuffle() on the array of cards. Overall, I wanted to create a well-designed game with code that met the criteria of being organized, modular, and well-factored. I believed that python was the best language to help me achieve these goals, because of its clean syntax and multitude of provided methods.
