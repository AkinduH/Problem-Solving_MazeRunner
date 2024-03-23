# Problem-Solving_MazeRunner

When you navigate through the maze, print the steps that you take in the following manner. An example output is shown below with explanation. Each line below ends with a new line.






![pasted image 0](https://github.com/AkinduH/Problem-Solving_MazeRunner/assets/164672047/5d552b11-df63-40fe-a6be-5b7656a3cf2a)















 

Start at ( 2 , 0 ) – enter into the maze from the cell at (2,0) coordinates.

North North East East East Stuck at ( 0 , 3 ) – starting from cell at (2,0), navigate to the North cell at (1,0). Then navigate to North cell (0,0), East cell (0,1), East cell (0,2), East cell (0,3) until you are stuck. Note that the order of the directions of traversing is defined as North, East, South, West.

Back to ( 0 , 2 ) – Since you could not continue from the cell at (0,3), get back to the cell at (0,2) where you can take a different path.

South East Stuck at ( 1 , 3 ) – starting from the cell at (0,2), move to South cell (1,2). Then move to East cell at (1,3) where you are stuck.

Back to ( 1 , 2 ) – backtrack to cell at (1,2) where you can take a different path.

.…

Stuck at ( 7 , 13 ) – you are stuck at the cell (7,13)

Back to ( 8 , 13 ) – backtrack to cell at (8,13) where you can take a different path.

South South South Leaving at ( 11 , 13 ) - starting from the cell at (8,13), move to the South cell (9,13). Then move to the South cell at (10,13), and to the South cell (11,13) where you can leave the maze.

 

The expected output after traversing the above maze is below:



For example:

Result
Start at ( 2 , 0 )

North North East East East Stuck at ( 0 , 3 )

Back to ( 0 , 2 )

South East Stuck at ( 1 , 3 )

Back to ( 1 , 2 )

West Stuck at ( 1 , 1 )

Back to ( 1 , 2 )

.
.
.
.
.

South South South Leaving at ( 11 , 13 )
