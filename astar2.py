from Solver import Solver
from Maze import Maze

game = Maze(3)
game.construct("7 2 4 5 0 6 8 3 1")

astar_solver = Solver(game)
astar_solver.a_star_second_heuristic()
