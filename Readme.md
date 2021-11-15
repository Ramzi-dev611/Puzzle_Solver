# PUZZLE SOLVER

This repository contains my take on the puzzle solving program using graph traversal algorithms: **bfs**, **dfs**,
**iterative dfs** and **A star**

Other than the test cases scripts the solution is made using two classes: 

## 1. MAZE
* This class represents the grid that we can decide it's size at construction level

* When the constructor is invoked, the object obtained will contain a solved grid

* The class Maze contains several methods: 
  * shuffle(): makes a 1000 random action on the grid to shuffle it
  * All possible actions implementations
  * check_solved(): returns true if the grid is at the goal state and false otherwise
  * to_string(): returns a string representation of the grid
  * two heuristic functions 
  * display(): displays the grid values on two dimensions
  * construct(grid : string): changes the grid to become compatible with the given string
* The first heuristic function returns the number of grid's elements that are not on their positions
* The second heuristic function returns the sum of the hamming distance between each element of the grid and it's supposed to be position

## 2. Solver
* This class gives the implementation of the four wanted algorithms
* For all the algorithms the state of the grid is represented by a string
* For the BFS :
  * The list of visited states is stored in a dictionary where the keys are the visited nodes and the values are the parent nodes their keys
  * The list of future examined states is stored in a deque where we append on the left side of it, states, and we pop states from the left side (something similar to a queue)
* For the DFS :
  * The list of visited states is stored in a dictionary where the keys are the visited nodes and the values are the parent nodes their keys
  * The list of future examined states is stored in a deque where we append on the right side of it, states, and we pop states from the left side (something similar to a stack)
* For the ITERATIVE DFS :
  * It's based on a call of DFS with each time increasing depth limit
* For the A STAR :
  * The list of visited states is stored in a dictionary where the keys are the visited nodes and the values are the parent nodes their keys
  * The list of future examined states is stored in as a heap. Each element of the heap contains the cost taken to reach the state presented by this element plus it's evaluation representing the states priority

=> This use of a dictionary for the visited nodes is intended to generate by the end of the search the path found by the algorithm called
