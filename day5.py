import string
import sys
sys.setrecursionlimit(5000)

def fn1(polymer):
    # Seems like it should be a recursive thing.
    # Run through once, then feed to itself to run again.
    # Base case is that the before and after lengths are the same.
    start_len = len(polymer)

    # Process it
    for letter in string.ascii_lowercase:
        polymer = polymer.replace(letter + letter.upper(), '').replace(letter.upper() + letter, '')

    if len(polymer) == start_len:
        return start_len
    return fn1(polymer)

def fn2(polymer):
    # First do each letter from the above list, and then use fn1
    # Keep track of running best.

    best = (None, len(polymer))
    for letter in string.ascii_lowercase:
        result = polymer.replace(letter, '').replace(letter.upper(), '')
        score = fn1(result)
        if score < best[1]:
            best = (letter, score)

    return best

if __name__ == '__main__':
    print(fn1("dabAcCaCBAcCcaDA"))
    print(fn2("dabAcCaCBAcCcaDA"))

    with open('day5.txt', 'r') as inpt:
        print(fn1(inpt.read().strip()))
        inpt.seek(0)
        print(fn2(inpt.read().strip()))
