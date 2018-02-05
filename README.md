# AIWithFriends

CS4341 Intro to AI
Project 1 C-term: Gomoku

Submitted to Professor Ahmedul Kabir
of the
Worcester Polytechnic Institute

by:
Jason Abel				Thomas Hagen 			Parmenion Patias

Date: 6 February 2018
 
Compiling and Running:

Our program was written in Python. To run the program one needs to have python installed on his system. Once this requirement is covered running the program is as easy as opening the command line, navigating to where the file is saved and typing “python *file_name” and hitting enter.

Utility Function:

Utility Function refers to the sum of preferences our agent has. In the case of our program the agent wants to have 5 continuous dots in a row, column or diagonally. It also wants to stop the opponent from doing 5 in a row, and it focuses on that the closer the opponent is to achieving his plan.

Evaluation Function:

For our evaluation function, we tried to focus on how important it is not to allow the opponent to do 5 consecutive dots. To stop that from happening in our evaluation function 1 added dot in the 5 row increases the importance of that line by 10.

Eval(J)=[∑▒(1000000*(# of 4 dots)) +∑▒(100000*(# of 3 dots)) +∑▒(1000*(# of 2 dots)) +∑▒(1*(# of 1 dots)) ]-[∑▒(1000000*(# of 4 dots)) +∑▒(100000*(# of 3 dots)) +∑▒(1000*(# of 2 dots)) +∑▒(1*(# of 1 dots)) ]

Heuristics & Strategies:

There are quite some specific actions our program takes:

1 if an opponent piece is 4 steps (or less) away from one of our pieces, the program doesn’t evaluate that piece.

2 if an opponent piece is 4 steps (or less) away from the border our program doesn’t evaluate that piece.

Results

Tests:

To test the integrity and reliability of our program we checked how it reacted and played in some specific cases. We tried to make sure the program can identify serious threats (eg. x-xxx, xx-xx, xxx-x) and react to stop them (eg. xoxxx, xxoxx, xxxox).

We also had the program play against a copy of itself, in order to make sure that the program is able to complete a game without making any illegal moves, and without making illogical moves.

Strengths & Weaknesses:

α-β pruning works great in games such as gomoku where evaluating the state of the game is difficult. α-β pruning works by checking all (or many) possible moves; it finds what the game would look like x number of steps down and it makes the best choice given a logical opponent that would go for the best move as well.

The time complexity and space complexity is quite big. Especially for an application in gomoku as the branching factor is quite big and every step we go deeper the calculations required increase greatly.
We assume that the opponent will play logically, thus a program made to make the second-best move, could potentially put us in risk, as its moves wouldn’t be always countered by our program.
α-β pruning calculates all possible moves even if they have low expected results, thus it takes time calculating how the outcome of a bad move, instead of focusing going deeper on a set of good move in order to find the best move possible.

Discussion (Evaluation and Heuristics):

α-β pruning need to examine on average O(b^(d⁄2) ) nodes. Which is much less than other techniques such as minimax for examples which would require checking O(b^d ) nodes to make a decision. Also, our program checks 3 steps ahead from our current position and makes a choice based on that. This is done so we always take less than 10 seconds to read the opponent’s move, and write our own move. Had we a better system, or more time to think and act we would allow the program to calculate more moves before making a choice.



