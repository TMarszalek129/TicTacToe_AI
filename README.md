# TicTacToe_AI
TicTacToe with AI players

<p>The game was implemented using easyAI module. Two AI players with variable depth configuration of Negamax 
or Expecti-minimax alghoritm are used.
Scores will be calculated and recorded once all games have been completed.
Elapsed time was printed after all games.
</p>

<hr>
<h2>PARAMETER possible_loss == True</h2>
<p>There is a 20% chance, that AI bot will fail. In that case, it loses its turn and 
the other one continues.</p>
<h2>PARAMETER possible_loss == False</h2>
<p>Classical game TicTacToe.</p>
<hr>

<h2>PARAMETER pruning == True</h2>
<p>Alpha-beta pruning modification is used.</p>
<h2>PARAMETER pruning == False</h2>
<p>Classical algorithm without alpha-beta pruning.</p>
<hr>

<h2>PARAMETER mode == 'negamax'</h2>
<p>Negamax algorithm is used to calculate the best turn for each AI players.</p>
<h2>PARAMETER mode == 'expecti'</h2>
<p>Expecti-minimax algorithm is used to calculate the best turn for each AI players.</p>
<hr>

<p>The results is printed in command prompt: </p>
<img src="img.png">