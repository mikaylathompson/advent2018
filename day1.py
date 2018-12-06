def fn1(inpt_lines):
    current_val = 0
    for line in inpt_lines:
        if line[0] == '-':
            current_val -= int(line[1:])
        else:
            current_val += int(line[1:])
    return current_val

def fn2(inpt_lines):
    current_val = 0
    seen_vals = set()
    while True:
        # print("First run through: ")
        for line in inpt_lines:
            # print("Line: ", line)
            if line[0] == '-':
                current_val -= int(line[1:])
            else:
                current_val += int(line[1:])
            # print("Current val: ", current_val)
            # print("\nSeen vals: ", seen_vals)
            if current_val in seen_vals:
                return current_val
            seen_vals.add(current_val)


if __name__ == '__main__':
    with open('day1.txt', 'r') as inpt:
        print(fn1(inpt.readlines()))
        inpt.seek(0)
        print(fn2(inpt.readlines()))
