def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def closest(target, points):
    # Need to deal with ties!
    distances = [distance(target, p) for p in points]
    best = min(range(len(distances)), key=lambda i: distances[i])
    if distances.count(best) > 1:
        return None
    return best

    # 3736 is TOO HIGH
    # 3612 is TOO LOW

def fn1(inpt_lines):
    points = [tuple(map(int, line.strip().split(', '))) for line in inpt_lines]
    # first order approx of dealing with infinity:
    # start 10 steps before/after/above/below most extreme points.
    # calculate all areas within this grid, and then knock out of contention any points represented on the edges

    border = 50
    min_x = min(p[0] for p in points) - border
    max_x = max(p[0] for p in points) + border
    min_y = min(p[1] for p in points) - border
    max_y = max(p[1] for p in points) + border
    counts = [0] * len(points)
    ineligible = set()
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            winner = closest((x, y), points)
            if winner is not None:
                counts[winner] += 1
                if x in [min_x, max_x] or y in [min_y, max_y]:
                    ineligible.add(winner)
    print("Pre correction: ", counts)
    print("Ineligible: ", ineligible)
    for bad in ineligible:
        counts[bad] = -1
    print("Corrected: ", counts)
    return max(counts)

def fn2(inpt_lines):
    return None

if __name__ == '__main__':
    with open('day6.txt', 'r') as inpt:
        print(fn1(inpt.readlines()))
        inpt.seek(0)
        print(fn2(inpt.readlines()))
