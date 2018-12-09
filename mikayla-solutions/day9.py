from collections import Counter

def steps_cw(ln, pos, steps):
    return (pos + steps) % ln

def fn1(players, last_marble):
    current_board = [0]
    scores = [0] * players
    active = 0
    current_marble = 0
    p = 0

    while True:
        p = (p + 1) % players
        if current_marble == last_marble:
            break
        current_marble += 1
        if (current_marble % 23 != 0):
            pos = steps_cw(len(current_board), active, 1)
            current_board = current_board[:pos+1] + [current_marble] + current_board[pos+1:]
            active = pos + 1
        else:
            scores[p] += current_marble
            pos = steps_cw(len(current_board), active, -7)
            scores[p] += current_board[pos]
            current_board = current_board[:pos] + current_board[pos+1:]
            active = pos

    print("High score: ", max(scores))
    return max(scores)

def fn2(inpt_lines):
    return None

if __name__ == '__main__':
    with open('../puzzle-input/day9_2018.txt', 'r') as inpt:
        # print(fn1(9, 25) == 32)
        # print(fn1(10, 1618) == 8317)
        # print(fn1(13, 7999) == 146373)
        # print(fn1(17, 1104) == 2764)
        # print(fn1(21, 6111) == 54718)
        # print(fn1(30, 5807) == 37305)
        print(fn1(416, 71617))
        inpt.seek(0)
        print(fn2(inpt.readlines()))
