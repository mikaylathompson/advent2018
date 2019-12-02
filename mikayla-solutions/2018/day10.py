import re
import string
from collections import namedtuple
import pprint

Point = namedtuple('Point', ['x', 'y'])
point_matcher = re.compile(r"position=< ?(?P<x>[-\d]+),\s+(?P<y>[-\d]+)>\svelocity=< ?(?P<vx>[-\d]+),\s+(?P<vy>[-\d]+)>")

def extract_points(inpt_lines):
    points = []
    for line in inpt_lines:
        match = point_matcher.match(line.strip())
        pos = Point(*map(int, match.group('x', 'y')))
        vel = Point(*map(int, match.group('vx', 'vy')))
        points.append([pos, vel])
    return points


def dimensions(points):
    return min([p[0].x for p in points]),\
            max([p[0].x for p in points]),\
            min([p[0].y for p in points]),\
            max([p[0].y for p in points])


def advance(points, time_steps=1):
    for p in points:
        p[0] = Point(p[0].x + (p[1].x * time_steps),
                     p[0].y + (p[1].y * time_steps))
    return points


def display(points, fname=""):
    def gprint(grid):
        if fname:
            with open(fname, 'w') as f:
                for row in grid:
                    print(''.join([cell for cell in row]), file=f)
            return
        for row in grid:
            print(''.join([cell for cell in row]))

    min_x, max_x, min_y, max_y = dimensions(points)
    grid = [[' '] * (max_x - min_x + 2) for x in range(max_y - min_y + 2)]
    for p, _ in points:
        try:
            grid[p.y - min_y][p.x - min_x] = "●"
        except IndexError:
            print(f"Index error with {p.x} and {p.y}. Trying to map to {p.y + min_y} and {p.x + min_x}")
            continue
    gprint(grid)
    

def fn1(inpt_lines): 
    points = extract_points(inpt_lines)
    best_dimensions = [0, 100000000]
    for i in range(12000):
        min_x, max_x, min_y, max_y = dimensions(points)
        area = (max_x - min_x) * (max_y - min_y)
        if area < best_dimensions[1]:
            best_dimensions = [i, area]
        advance(points, 1)
    # points = extract_points(inpt_lines)
    advance(points, -12000)
    advance(points, best_dimensions[0])
    print(best_dimensions[0])
    display(points)#, "day10-output.txt")

def fn2(inpt_lines):
    return None

if __name__ == '__main__':
    with open('../puzzle-input/day10_2018.txt', 'r') as f:
        inpt_lines = f.read().splitlines()

    fn1(inpt_lines)
