#!/usr/bin/env python3

import heapq


def astar(start, goal):

    nodes = []

    class Node:
        def __init__(self, state, parent = None, dg = 0):
            self.state = state
            self.parent = parent
            if parent is None:
                self.g = 0
            else:
                self.g = parent.g + dg

        def __lt__(self, other):
            return self.h() < other.h()

        def h(self):
            return self.g + self.state.distance(goal)

    frontier = []

    def addNode(state, parent = None, dg = 0):
        node = Node(state, parent, dg)
        nodes.append(node)
        heapq.heappush(frontier, (node.h(), node))

    def get_same(state, queue):
        twins = [twin for twin in queue if twin.state == state]
        if twins:
            return min(twins, key = lambda t: t.g)
        return None

    addNode(start)

    closed = []
    max_iter = 500
    it = 0
    while frontier:
        it += 1

        if it == max_iter:
            return None

        best = heapq.heappop(frontier)[1]

        if best.state == goal:
            break
        closed.append(best)

        for child in best.state.children():

            child_g = best.g + child.dist2parent

            visited = get_same(child, closed)
            if visited is not None:
                if visited.g > child_g:
                    addNode(child, best, child.dist2parent)
                continue

            twin = get_same(child, nodes)
            if twin is not None:
                if twin.g > child_g:
                    addNode(child, best, child.dist2parent)
            else:
                addNode(child, best, child.dist2parent)

    # reverse
    path = []
    while True:
        path.insert(0, best.state)
        if best.parent is None:
            break
        best = best.parent

    return path
