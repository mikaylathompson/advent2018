import re
import datetime
from collections import defaultdict, Counter

event_re = re.compile(r"\[(?P<dt>.*)\] (?P<text>(Guard #(?P<gid>\d+) )?.*)")

def process_event_stream(inpt_lines):
    # Apply regex to each line.
    # First pass: process datetime, and add a tuple of (dt, guard, text). First pass, many guards will be None.
    # Second pass: Sort, fill in guard details. New tuple: (dt, guard, action, minutes-since-last)
    # Would be better with namedtuples

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
    # print(first_pass)
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
    sleep_time = defaultdict(int)
    for event in event_stream:
        if event[2] == 'wake': # this means the last period of time was sleeping
            sleep_time[event[1]] += event[3]

    sleepiest_guard = max(sleep_time, key=sleep_time.get)
    # print(sleep_time)
    # print(sleepiest_guard)

    # Now, for all 'wake' events involving that guard, count which minutes are asleep
    relevant_events = filter(lambda x: x[1] == sleepiest_guard and x[2] == 'wake', event_stream)
    minute_counts = Counter()
    for event in relevant_events:
        minute_counts.update(range(event[0].minute - event[3], event[0].minute))
    return minute_counts.most_common(1)[0][0] * sleepiest_guard

def fn2(inpt_lines):
    return None

if __name__ == '__main__':
    with open('day4.txt', 'r') as inpt:
        event_stream = process_event_stream(inpt.readlines())
        # print(fn1(inpt.readlines()))
        print(fn1(event_stream))
        inpt.seek(0)
        print(fn2(inpt.readlines()))
