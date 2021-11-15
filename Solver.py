import collections
import heapq
import re
from Maze import Maze


class Solver:
    def __init__(self, maze : Maze):
        self.maze = maze

    def draw_path(self, visited: dict, solution: str):
        path = collections.deque([])
        key = solution
        while key != '':
            path.append(key)
            key = visited[key]
        print("Solution depth = "+str(len(path)))
        node = Maze(self.maze.size)
        if len(path) < 51:
            while path:
                string = path.pop()
                node.construct(string)
                node.display()
        else:
            print("path too long")

    def bfs(self):
        queue = collections.deque([self.maze.__toString__()])
        visited = {self.maze.__toString__(): ''}
        counter = 0
        node_maze = Maze(self.maze.size)
        while queue:
            node_string = queue.pop()
            node_maze.construct(node_string)
            if node_maze.__checkSolved__():
                print("solution found after visiting "+str(counter)+" node")
                print("Path Found")
                self.draw_path(visited, node_string)
                break
            if node_maze.move_left() == 1:
                if not node_maze.__toString__() in visited :
                    queue.appendleft(node_maze.__toString__())
                    visited[node_maze.__toString__()] = node_string
                node_maze.move_right()
            if node_maze.move_right() == 1:
                if not node_maze.__toString__() in visited:
                    queue.appendleft(node_maze.__toString__())
                    visited[node_maze.__toString__()] = node_string
                node_maze.move_left()
            if node_maze.move_down() == 1:
                if not node_maze.__toString__() in visited :
                    queue.appendleft(node_maze.__toString__())
                    visited[node_maze.__toString__()] = node_string
                node_maze.move_up()
            if node_maze.move_up() == 1:
                if not node_maze.__toString__() in visited:
                    queue.appendleft(node_maze.__toString__())
                    visited[node_maze.__toString__()] = node_string
                node_maze.move_down()
            counter = counter + 1

    def dfs(self):
        queue = collections.deque([self.maze.__toString__()])
        visited = {self.maze.__toString__(): ''}
        counter = 0
        node_maze = Maze(self.maze.size)
        while queue:
            node_string = queue.pop()
            node_maze.construct(node_string)
            if node_maze.__checkSolved__():
                print("solution found after visiting "+str(counter)+" node")
                print("Path Found")
                self.draw_path(visited, node_string)
                break
            if node_maze.move_left():
                if not node_maze.__toString__() in visited:
                    queue.append(node_maze.__toString__())
                    visited[node_maze.__toString__()] = node_string
                node_maze.move_right()
            if node_maze.move_right():
                if not node_maze.__toString__() in visited:
                    queue.append(node_maze.__toString__())
                    visited[node_maze.__toString__()] = node_string
                node_maze.move_left()
            if node_maze.move_down():
                if not node_maze.__toString__() in visited:
                    queue.append(node_maze.__toString__())
                    visited[node_maze.__toString__()] = node_string
                node_maze.move_up()
            if node_maze.move_up():
                if not node_maze.__toString__() in visited:
                    queue.append(node_maze.__toString__())
                    visited[node_maze.__toString__()] = node_string
                node_maze.move_down()
            counter = counter + 1

    def dfs_limit(self, limit: int):
        queue = collections.deque([(self.maze.__toString__(), limit)])
        visited = {self.maze.__toString__(): ''}
        counter = 0
        node_maze = Maze(self.maze.size)
        while queue:
            (node_string, l) = queue.pop()
            node_maze.construct(node_string)
            if node_maze.__checkSolved__():
                print("solution found after visiting " + str(counter) + " node")
                print("Path Found")
                self.draw_path(visited, node_string)
                return 1
            if l > 0:
                if node_maze.move_left():
                    if node_maze.__toString__() not in visited:
                        queue.append((node_maze.__toString__(), l - 1))
                        visited[node_maze.__toString__()] = node_string
                    node_maze.move_right()
                if node_maze.move_right():
                    if node_maze.__toString__() not in visited:
                        queue.append((node_maze.__toString__(), l - 1))
                        visited[node_maze.__toString__()] = node_string
                    node_maze.move_left()
                if node_maze.move_down():
                    if node_maze.__toString__() not in visited:
                        queue.append((node_maze.__toString__(), l - 1))
                        visited[node_maze.__toString__()] = node_string
                    node_maze.move_up()
                if node_maze.move_up():
                    if node_maze.__toString__() not in visited:
                        queue.append((node_maze.__toString__(), l - 1))
                        visited[node_maze.__toString__()] = node_string
                    node_maze.move_down()
            counter = counter + 1
        return 0

    def dfs_iterative(self):
        limit = 0
        while True:
            if self.dfs_limit(limit) == 1:
                break
            limit = limit + 1

    def a_star_first_heuristic(self):
        queue = [(maze.heuristic1(), maze.__toString__(), 0)]
        heapq.heapify(queue)
        visited = {self.maze.__toString__(): ''}
        counter = 0
        node_maze = Maze(self.maze.size)
        while queue:
            (evaluation, element, cost) = heapq.heappop(queue)
            node_maze.construct(element)
            if node_maze.__checkSolved__():
                print("solution found after visiting " + str(counter) + " node")
                print("Path Found")
                self.draw_path(visited, element)
                break
            if node_maze.move_left():
                if node_maze.__toString__() not in visited:
                    heapq.heappush(queue, (node_maze.heuristic1() + cost + 1, node_maze.__toString__(), cost + 1))
                    visited[node_maze.__toString__()] = element
                node_maze.move_right()
            if node_maze.move_right():
                if node_maze.__toString__() not in visited:
                    heapq.heappush(queue, (node_maze.heuristic1() + cost + 1, node_maze.__toString__(), cost + 1))
                    visited[node_maze.__toString__()] = element
                node_maze.move_left()
            if node_maze.move_down():
                if node_maze.__toString__() not in visited:
                    heapq.heappush(queue, (node_maze.heuristic1() + cost + 1, node_maze.__toString__(), cost + 1))
                    visited[node_maze.__toString__()] = element
                node_maze.move_up()
            if node_maze.move_up():
                if node_maze.__toString__() not in visited:
                    heapq.heappush(queue, (node_maze.heuristic1() + cost + 1, node_maze.__toString__(), cost + 1))
                    visited[node_maze.__toString__()] = element
                node_maze.move_down()
            counter += 1

    def a_star_second_heuristic(self):
        queue = [(maze.heuristic2(), maze.__toString__(), 0)]
        heapq.heapify(queue)
        visited = {self.maze.__toString__(): ''}
        counter = 0
        node_maze = Maze(self.maze.size)
        while queue:
            (evaluation, element, cost) = heapq.heappop(queue)
            node_maze.construct(element)
            if node_maze.__checkSolved__():
                print("solution found after visiting " + str(counter) + " node")
                print("Path Found")
                self.draw_path(visited, element)
                break
            if node_maze.move_left():
                if node_maze.__toString__() not in visited:
                    heapq.heappush(queue, (node_maze.heuristic2() + cost + 1, node_maze.__toString__(), cost + 1))
                    visited[node_maze.__toString__()] = element
                node_maze.move_right()
            if node_maze.move_right():
                if node_maze.__toString__() not in visited:
                    heapq.heappush(queue, (node_maze.heuristic2() + cost + 1, node_maze.__toString__(), cost + 1))
                    visited[node_maze.__toString__()] = element
                node_maze.move_left()
            if node_maze.move_down():
                if node_maze.__toString__() not in visited:
                    heapq.heappush(queue, (node_maze.heuristic2() + cost + 1, node_maze.__toString__(), cost + 1))
                    visited[node_maze.__toString__()] = element
                node_maze.move_up()
            if node_maze.move_up():
                if node_maze.__toString__() not in visited:
                    heapq.heappush(queue, (node_maze.heuristic2() + cost + 1, node_maze.__toString__(), cost + 1))
                    visited[node_maze.__toString__()] = element
                node_maze.move_down()
            counter += 1
