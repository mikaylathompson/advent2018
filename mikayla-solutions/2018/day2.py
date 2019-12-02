from collections import Counter

def fn1(inpt_lines):
    twos = 0
    threes = 0
    for line in inpt_lines:
        cnt = Counter(line)
        if 2 in cnt.values():
            twos += 1
        if 3 in cnt.values():
            threes += 1
    return twos * threes

def fn2(inpt_lines):
    # Add entries to a dictionary in form:
        # {"*bcde": ["abcde", "xbcde", "yxcde"], "a*cde": ["abcde"], "ab*de": ["abcde"] ...}
    # Actually, I can do it as a set, and if I ever find a match, that's the correct one.
    prototypes = set()
    for word in inpt_lines:
        word = word.strip()
        for i in range(len(word) - 1):
            new_word = "{0}*{1}".format(word[:i], word[i+1:])
            if new_word in prototypes:
                return new_word.replace('*', '')
            prototypes.add(new_word)
    return None

if __name__ == '__main__':
    with open('../puzzle-input/day2_2018.txt', 'r') as inpt:
        print(fn1(inpt.readlines()))
        inpt.seek(0)
        print(fn2(inpt.readlines()))
