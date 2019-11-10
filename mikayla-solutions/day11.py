from functools import lru_cache

@lru_cache(maxsize=None)
def calc_power(x, y, sn):
    # Find the fuel cell's rack ID, which is its X coordinate plus 10.
    rack_id = x + 10
    # Begin with a power level of the rack ID times the Y coordinate.
    power_level = rack_id * y
    # Increase the power level by the value of the grid serial number (your puzzle input).
    power_level += sn
    # Set the power level to itself multiplied by the rack ID.
    power_level *= rack_id
    # Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
    power_level = power_level // 100 % 10
    # Subtract 5 from the power level.
    power_level -= 5
    return power_level

def display(points, fname=""):
    for p, v in points.items():
        if p[0][1] == 1:
            print()
        print(f"{v: >4}", end="") #print(p)
    print()

def components(x, y, size=3):
    return [(x+xa, y+ya) for xa in range(0, size) for ya in range(0, size)]

def fn1(sn, dim=300): 
    toplefts = [(x, y) for x in range(1, 298) for y in range(1, 298)]
    # powers = {}
    best = [(0, 0), 0]
    for tl in toplefts:
        power = sum([calc_power(*pos, sn) for pos in components(*tl)])
        if power > best[1]:
            best = (tl, power)
    return best

def fn2(sn, dim=300):
    filled_grid = {}
    for pos in [(x, y) for x in range(1, dim+1) for y in range(1, dim+1)]:
         filled_grid[(pos, 1)] = calc_power(*pos, sn)

    display(filled_grid)

    toplefts = [(x, y) for x in range(1, dim) for y in range(1, dim)]

    best_pos = max(filled_grid.keys(), key=lambda x: filled_grid[x])
    best = [*best_pos, filled_grid[best_pos]]

    for size in range(2, dim):
        for z in [2, 3, 5, 7, 11, 13, 17]:
            if size > z and size % z == 0:
                factor = size // z
                sub_toplefts = [(xa, ya) for xa in range(0, size, factor) for ya in range(0, size, factor)]
                factors = [factor] * len(sub_toplefts)
                break
        else:
            if size < 5:
                factor = 1
                sub_toplefts = [(xa, ya) for xa in range(0, size, factor) for ya in range(0, size, factor)]
                factors = [factor] * len(sub_toplefts)
            else:
                sub_toplefts = [(0, 0)] + [(xa, size-1) for xa in range(0, size - 1)] + [(size-1, ya) for ya in range(0, size)]
                factors = [size] + [1] * (len(sub_toplefts) - 1)

        for tl in toplefts:
            try:
                power = sum([filled_grid[((tl[0] + stl[0], tl[1] + stl[1]), factors[i])] for i, stl in enumerate(sub_toplefts)])
            except KeyError:
                continue
            except AssertionError:
                print([pos for pos in [(tl[0]+xa, tl[1]+ya) for xa in range(0, size, factor) for ya in range(0, size, factor)]])
                print([filled_grid[(pos, factor)] for pos in [(tl[0]+xa, tl[1]+ya) for xa in range(0, size, factor) for ya in range(0, size, factor)]])
                print([calc_power(*pos, sn) for pos in components(*tl, size=size)])
                continue
            filled_grid[(pos, size)] = power
            if power > best[2]:
                best = (tl, size, power)
        print(f"At size: {size}, best is: {best}")
    print()
    return best

## Load input data and run our two main functions
if __name__ == '__main__':
    with open('../puzzle-input/day11_2018.txt', 'r') as file:
        inpt_lines = file.read().splitlines()

    # Fuel cell at  122,79, grid serial number 57: power level -5.
    # Fuel cell at 217,196, grid serial number 39: power level  0.
    # Fuel cell at 101,153, grid serial number 71: power level  4.

    # print(calc_power(122, 79, 57) == -5)
    # print(calc_power(217, 196, 39) == 0)
    # print(calc_power(101, 153, 71) == 4)

    # print(components(0, 0))
    # print(components(100, 100))
    # print(components(298, 139))

    # print(fn1(18) == ((33, 45), 29))
    # print(fn1(42) == ((21, 61), 30))
    # print(fn1(9306))

    # For grid serial number 18, the largest total square (with a total power of 113) is 16x16 and has a top-left corner of 90,269, so its identifier is 90,269,16.
    # For grid serial number 42, the largest total square (with a total power of 119) is 12x12 and has a top-left corner of 232,251, so its identifier is 232,251,12.

    # print(fn2(18) == ((90,269),16, 113))
    # print(fn2(42) == ((232,251),12, 119))
    print(fn2(9306, dim=30))
