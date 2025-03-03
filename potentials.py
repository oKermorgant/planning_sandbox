
from circles import Circle
from numpy import log


class Potential:

    def __init__(self, circles):
        self.circles = circles

    def compute(self):

        Kp = 0.1
        Ka = 2.

        v = []

        for c in self.circles:
            dx, dy = c.err()
            d = dx**2+dy**2
            gain = max(1,5-log(d+1))
            obs = min(d,1)
            vx = dx*Kp*gain
            vy = dy*Kp*gain

            for c2 in self.circles:
                if c is c2:
                    continue
                margin = 1.5*(c.r + c2.r) / c.dist(c2)
                if margin > 1:
                    vx += Ka * obs * (c.x-c2.x)*log(margin)
                    vy += Ka * obs * (c.y-c2.y)*log(margin)

            v.append((vx,vy))
        return v

    def move(self, dt = 0.1):

        vmax = 0
        v = self.compute()

        for i,(vx,vy) in enumerate(v):
            self.circles[i].move(dt*vx,dt*vy)
            vmax = max(vmax,max(abs(vx),abs(vy)))
        return vmax
