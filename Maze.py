import numpy as np
import random


class Maze:
    def __init__(self, size):
        self.size = size
        self.map = np.arange(0, size ** 2).reshape(self.size, self.size)

    def shuffle(self):
        moves = 100
        for move in range(moves):
            action = random.randint(0, 4)
            if action == 0:
                self.move_up()
            elif action == 1:
                self.move_right()
            elif action == 2:
                self.move_down()
            else:
                self.move_left()

    def move_left(self):
        (x0, y0) = np.argwhere(self.map == 0)[0]
        if y0 == 0:
            return 0
        else:
            element = self.map[x0, y0 - 1]
            self.map[x0, y0 - 1] = 0
            self.map[x0, y0] = element
        return 1

    def move_right(self):
        (x0, y0) = np.argwhere(self.map == 0)[0]
        if y0 == self.size - 1:
            return 0
        else:
            element = self.map[x0, y0 + 1]
            self.map[x0, y0 + 1] = 0
            self.map[x0, y0] = element
        return 1

    def move_up(self):
        (x0, y0) = np.argwhere(self.map == 0)[0]
        if x0 == 0:
            return 0
        else:
            element = self.map[x0 - 1, y0]
            self.map[x0 - 1, y0] = 0
            self.map[x0, y0] = element
        return 1

    def move_down(self):
        (x0, y0) = np.argwhere(self.map == 0)[0]
        if x0 == self.size - 1:
            return 0
        else:
            element = self.map[x0 + 1, y0]
            self.map[x0 + 1, y0] = 0
            self.map[x0, y0] = element
        return 1

    def __checkSolved__(self):
        string = ""
        for number in range(self.size ** 2):
            string = string + str(number) + " "
        return self.__toString__() == string[:-1]

    def __toString__(self):
        string = ""
        for el in self.map:
            for s in el:
                string = string + str(s) + " "
        return string[:-1]

    def display(self):
        print(self.map)

    def heuristic1(self):
        elements = self.__toString__().split(' ')
        supposed_to_be = 0
        h = 0
        for element in elements:
            if int(element) != supposed_to_be and int(element) != 0:
                h = h + 1
            supposed_to_be = supposed_to_be + 1
        return h

    def heuristic2(self):
        elements = self.__toString__().split(' ')
        goal = np.arange(0, self.size ** 2)
        h = 0
        for index in range(self.size ** 2):
            element = int(elements[index])
            if element == 0:
                continue
            yi = int(index / self.size)
            xi = index % self.size
            goal_position = np.argwhere(goal == element)[0]
            xg = goal_position % self.size
            yg = int(goal_position / self.size)
            h = h + abs(xg - xi) + abs(yg - yi)
        return h

    def construct(self, map_description: str):
        self.map = np.array(map_description.split(' '), dtype=int).reshape(self.size, self.size)

