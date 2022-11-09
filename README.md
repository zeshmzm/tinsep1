# There is No Spoon - Episode 1

This project is about finding a solution of nodes in a rectangular grid (2x2 used here). The coding test link from codingame is given below:

https://www.codingame.com/ide/puzzle/there-is-no-spoon-episode-1

The code was not completed due to time constraints. But, it is ready for enhacements.

## The Problem
The solution is to find two nodes; one to the right of the input node and the other to the bottom of it. In short, coordinates of the nodes are to be found to ascertain their exact location in the rectangular grid.
In input, the width and height of the rectangular grid are to be given. The code was tested at the 2x2 rectangular grid. A variable ‘line’ for width characters is also taken. A cell that has 0 means a valid node and dot for the empty one. The solution should be given like this:

                                             1  2  3  4  5  6

## Tools Used
Python was used as the core language to perform this task. The following libraries were taken use of during the process.
- Numpy
-	Sys
## The Approach
Before going ahead, knowledge of python and some of its core libraries like Numpy is needed. For this programming quiz, a simple and straightforward approach was devised. Following are the list of steps taken to find the solution:
- The width and height are given first alongside line of width characters.
- Line can only take 0 or 1 as its values.
-	A method compute_neighbour() is made for printing the final output.
-	After starting with a random binary coordinate, efforts are made to find its right neighbor and then its bottom neighbour. Both are entered and printed out at the end in the order explained above.
-	For the coordinate in the corner, there isn’t any coordinate that exists. Those values at the right and the bottom are to be replaced by the -1 value to show that no such node exists at that coordinate.

##Running the Project
If you intend to run the project at codingame, you simply need to copy the code and paste it there on the project quiz link given above. For the local running, you need to have a Python IDE installed like Jupyter Notebook etc.
One also needs to have all the required libraries properly installed and imported. Numpy doesn’t come with the official Python package. So, it has to be installed and imported manually. The sys library comes packaged with the Python tool. The libraries can be installed with the following command:

                                          pip install {library-name}

For Jupyter Notebook, add a ! or a % at the start of the index tab before running the terminal command. If you intend to run it directly in the terminal, you can use the command as it is.

## Learnings from this Test
The aim of this test was to find a solution that fits. The main aim was not to find the best solution possible for it. So, as an open-source piece of code, one is free to modify it and make changes to it to have a better output if they want.
