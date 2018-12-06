import re
import datetime

event_re = re.compile(r"\[(?P<dt>.*)\] (?P<text>(Guard #(?P<gid>\d+) )?.*)")

def process_event_stream(inpt_lines):
    # Apply regex to each line.
    # First pass: process datetime, and add a tuple of (dt, guard, text). First pass, many guards will be None.
    # Second pass: Sort, fill in guard details. New tuple: (dt, guard, action, minutes-since-last)

    # First pass
    first_pass = []
    for line in inpt_lines:
        event = event_re.match(line)
        dt = datetime.datetime.fromisoformat(event.group('dt'))
        try:
            gid = int(event.group('gid'))
        except:
            gid = None
        first_pass.append((dt, gid, event.group('text')))
    print(first_pass)
    second_pass = []
    current_guard = None
    last_time = sorted(first_pass)[0][0]
    for event in sorted(first_pass):
        if event[1] is not None:
            current_guard = event[1]
        delta = (event[0] - last_time).seconds // 60
        if 'wakes' in event[2]:
            action = 'wake'
        elif 'asleep' in event[2]:
            action = 'sleep'
        else:
            action = 'begins'
        second_pass.append((event[0], current_guard, action, delta))
        last_time = event[0]
    return second_pass

def fn1(event_stream):
    # Count sleeping time per guard
    return None

def fn2(inpt_lines):
    return None

if __name__ == '__main__':
    with open('test_day4.txt', 'r') as inpt:
        event_stream = process_event_stream(inpt.readlines())
        # print(fn1(inpt.readlines()))
        print(fn1(event_stream))
        inpt.seek(0)
        print(fn2(inpt.readlines()))
