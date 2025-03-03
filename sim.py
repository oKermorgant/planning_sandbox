#!/usr/bin/env python3

from circles import Circle
import pylab as pl
import numpy as np
from potentials import Potential
from numpy.random import rand

size = 15
pl.close('all')
pl.figure(figsize=(6, 6))
ax = pl.gca()
pl.axis((-size, size, -size, size))


def border(color):
    ax.plot([-size, -size, size, size, -size], [-size, size, size, -size, -size], color, linewidth=4)


border('k')

ax.set_aspect('equal')
ax.axis('off')
pl.tight_layout()
pl.ion()
pl.show()

Planner = Potential


def generate(n):

    pos = size - 1.5

    def get_valid():
        
        while True:
            
            circles = []
            for _ in range(n):
                circles .append(Circle(-pos+2*pos*rand(), -pos+2*pos*rand(), 1, True))
            if Circle.minDist(circles) > .2:
                return circles
    
    circles = get_valid()
    end = get_valid()
    Circle.reset()
    for i, c in enumerate(circles):
        c.set_target(end[i].x, end[i].y)
    return circles


circles = generate(10)

planner = Planner(circles)


for it in range(2000):

    v = planner.move()

    if v < 0.001:
        border('b')
        print('local min after', it, 'iterations')
        break

    if Circle.minDist(circles) <= 0:
        border('r')
        break
    
    if all([np.linalg.norm(c.err()) < 0.1 for c in circles]):
        border('g')
        print('done in', it, 'iterations')
        break

    pl.pause(0.05)

