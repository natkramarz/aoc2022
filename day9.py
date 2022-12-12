from enum import Enum

class Direction(Enum):
    UP = ('U', 1, 0)
    DOWN = ('D', -1, 0)
    RIGHT = ('R', 0, 1)
    LEFT = ('L', 0, -1)

class Point():
    def __init__(self, row, col):
        self.row = row
        self.col = col
'''
with open("tests/day9.txt") as f:
    s = (0, 0)
    tail_points = set()
    tail_points.add(s)
    tail = Point(s[0], s[1])
    head = Point(s[0], s[1])
    tail_points.add((tail.row, tail.col))
    for line in f:
        line = line.rstrip()
        steps_direction, steps = line.split(' ')
        steps = int(steps)
        for direction in Direction:
            if steps_direction == direction.value[0]:
                row, col = direction.value[1], direction.value[2]
        for _ in range(steps):
            head.row += row
            head.col += col
            if abs(head.row - tail.row) == 2:
                if head.col != tail.col:
                    tail.col = head.col 
                tail.row += 1 if head.row - tail.row > 0 else -1
            elif abs(head.col - tail.col) == 2:
                if head.row != tail.row:
                    tail.row = head.row
                tail.col += 1 if head.col - tail.col > 0 else -1
            tail_points.add((tail.row, tail.col))
    print(len(tail_points))
'''
with open("tests/day9.txt") as f:
    s = (0, 0)
    motions = set()
    knots = [Point(0, 0),Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0)]
    motions.add((knots[9].row, knots[9].col))
    for line in f:
        line = line.rstrip()
        steps_direction, steps = line.split(' ')
        steps = int(steps)
        for direction in Direction:
            if steps_direction == direction.value[0]:
                row, col = direction.value[1], direction.value[2]
        for _ in range(steps):
            knots[0].row += row
            knots[0].col += col
            for i in range(1, len(knots)):
                if abs(knots[i-1].row - knots[i].row) == 2:
                    if knots[i-1].col != knots[i].col:
                        if (abs(knots[i-1].col - knots[i].col) == 2):
                            knots[i].col += 1 if knots[i-1].col - knots[i].col > 0 else -1
                        else:    
                            knots[i].col = knots[i-1].col 
                    knots[i].row += 1 if knots[i-1].row - knots[i].row > 0 else -1
                elif abs(knots[i-1].col - knots[i].col) == 2:
                    if knots[i-1].row != knots[i].row:
                        if abs(knots[i-1].row - knots[i].row) == 2:
                            knots[i].row += 1 if knots[i-1].row - knots[i].row > 0 else -1
                        else:
                            knots[i].row = knots[i-1].row
                    knots[i].col += 1 if knots[i-1].col - knots[i].col > 0 else -1
            motions.add((knots[9].row, knots[9].col))
    print(len(motions))