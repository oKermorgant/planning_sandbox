from circles import Circle
from numpy import log

class Potential:

    def __init__(self, circles):
        self.circles = circles

    def move(self):
        Kp = 0.05
        Ka = 1.5

        vmax = 0

        for c in self.circles:
            dx, dy = c.err()
            d = dx**2+dy**2
            gain = max(1,5-log(d+1))
            obs = min(d,1)
            dx *= Kp*gain
            dy *= Kp*gain

            for c2 in self.circles:
                if c is c2:
                    continue
                margin = 1.5*(c.r + c2.r) / c.dist(c2)
                if margin > 1:
                    dx += Ka * obs * (c.x-c2.x)* log(margin)
                    dy += Ka * obs * (c.y-c2.y)* log(margin)

            c.move(dx, dy)
            vmax = max(vmax,max(abs(dx),abs(dy)))
        return vmax