#!/usr/bin/env python3

import pylab as pl
import numpy as np


class Circle:
    t = pl.linspace(0, 2 * np.pi, 100)
    count = 0

    @staticmethod
    def minDist(circles):
        d = 300
        for i, c1 in enumerate(circles[:-1]):
            for c2 in circles[i+1:]:
                d = min(d, c1.dist(c2) - c1.r - c2.r)
        return d

    @staticmethod
    def reset():
        Circle.count = 0

    def __init__(self, x, y, r, display = False, static = False):
        self.x = x
        self.y = y
        self.r = r
        self.display = display
        self.static = static
        Circle.count += 1
        
    def err(self):
        return self.xd-self.x, self.yd-self.y

    def set_target(self, x, y):
        self.xd = x
        self.yd = y

        if self.display:
            if self.static:
                pl.plot(self.x + self.r * np.cos(self.t), self.y + self.r * np.sin(self.t), 'k', linewidth=2)
            else:
                self.contour = pl.plot(self.x + self.r * np.cos(self.t), self.y + self.r * np.sin(self.t))[0]
            color = self.contour.get_color()
            pl.plot(self.xd + self.r * np.cos(self.t), self.yd + self.r * np.sin(self.t), color, linestyle='dashed')

    def move(self, dx, dy):
        if self.static:
            return
        vmax = 2
        v = np.sqrt(dx**2 + dy**2)
        if v > vmax:
            dx *= vmax/v
            dy *= vmax/v

        self.x += dx
        self.y += dy
        self.draw()

    def draw(self):
        if self.display:
            self.contour.set_data(self.x + self.r * np.cos(self.t), self.y + self.r * np.sin(self.t))
            pl.draw()

    def dist(self, other):
        return np.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def collides(self, other):
        d = (self.x - other.x) ** 2 + (self.y - other.y) ** 2
        return d < (self.r + other.r)**2

