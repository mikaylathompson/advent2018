import re

clm_re = re.compile(r"#(?P<id>\d+) @ (?P<left>\d+),(?P<top>\d+): (?P<width>\d+)x(?P<height>\d+)")

def fn1(inpt_lines):
    # Once-seen and twice-seen sets. Once a square is seen, it's added to the once-seen set as "{left}-{right}".
    # If it's seen again, it's added to the twice-seen set.
    # 96477 is TOO LOW
    once_seen = set()
    twice_seen = set()
    for line in inpt_lines:
        claim = clm_re.match(line.strip())
        left, top, width, height = map(int, claim.group('left', 'top', 'width', 'height'))
        for x in range(left, left+width):
            for y in range(top, top+height):
                pos = "{x}-{y}".format(x=x, y=y)
                if pos in once_seen:
                    twice_seen.add(pos)
                once_seen.add(pos)
    return len(twice_seen)

def fn2(inpt_lines):
    once_seen = set()
    twice_seen = set()
    claims = {}
    for line in inpt_lines:
        claim = clm_re.match(line.strip())
        left, top, width, height = map(int, claim.group('left', 'top', 'width', 'height'))
        claim_set = set()
        for x in range(left, left+width):
            for y in range(top, top+height):
                pos = "{x}-{y}".format(x=x, y=y)
                claim_set.add(pos)
                if pos in once_seen:
                    twice_seen.add(pos)
                once_seen.add(pos)
        claims[claim.group('id')] = claim_set
    for claim in claims.keys():
        if claims[claim].isdisjoint(twice_seen):
            return claim
    return None

if __name__ == '__main__':
    with open('../puzzle-input/day3_2018.txt', 'r') as inpt:
        print(fn1(inpt.readlines()))
        inpt.seek(0)
        print(fn2(inpt.readlines()))
