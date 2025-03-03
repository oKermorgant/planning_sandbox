#!/usr/bin/env python3

from astar import astar
import numpy as np
from pylab import plot


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # used for heuristic
    def distance(self, other):
        return np.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    # used to check visited nodes + the goal
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # should return a list of (child, distance to parent)
    def children(self):
        ret = []

        for dx in (-1,0,1):
            for dy in (-1,0,1):
                if dx == 0 and dy == 0:
                    continue

                x = self.x+dx
                y = self.y+dy
                d = np.sqrt(dx**2+dy**2)

                # obstacle @ (5,5) size 3

                if (x-4)**2+(y-6)**2 < 10:
                    continue

                ret.append((Point(self.x+dx,self.y+dy), d))

        return ret


start = Point(0,0)
goal = Point(11,13)

path = astar(start, goal)

plot([p.x for p in path],[p.y for p in path])
