#!/usr/bin/env python3

from astar import astar
import numpy as np


class Point:
    def __init__(self, x, y, dist2parent = 0):
        self.x = x
        self.y = y
        self.dist2parent = 0

    def distance(self, other):
        return np.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def children(self):
        ret = []

        for dx, dy in ((-1,0), (1,0),(0,-1),(0,1)):

            x = self.x+dx
            y = self.y+dy

            # obstacle @ (5,5) size 3

            if (x-7)**2+(y-10)**2 < 10:
                continue

            ret.append(Point(self.x+dx,self.y+dy, 1))

        return ret


start = Point(0,0)
goal = Point(11,13)

path = astar(start, goal)
