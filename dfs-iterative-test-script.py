from Solver import Solver
from Maze import Maze

game = Maze(3)
game.construct("7 2 4 5 0 6 8 3 1")

dfs_iterative_solver = Solver(game)
dfs_iterative_solver.dfs_iterative()
