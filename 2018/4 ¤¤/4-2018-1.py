from collections import namedtuple
from datetime import datetime
import heapq

event = namedtuple('event', ['time', 'action', 'guard'])

events = []
guard_sleeps = {}

with open('4-input') as f:
    for line in f.readlines():
        time = datetime.strptime(line[1:17], '%Y-%m-%d %H:%M')
        
        action, guard = None, None

        match line[19]:
            case 'G':
                action = 'new shift'
                guard = int(line.split()[3][1:])
                guard_sleeps[guard] = [0] * 60
            case 'f':
                action = 'sleep'
            case 'w':
                action = 'wake'
        
        heapq.heappush(events,event(time,action,guard))

active_guard = None
sleep_time = None

while events:
    current_event = heapq.heappop(events)

    if sleep_time:
        minutes_asleep = 0
        wake_time = current_event.time.minute

        if current_event.action == 'wake':
            minutes_asleep = wake_time - sleep_time.minute
        else:
            minutes_asleep = 60 - sleep_time.minute
            wake_time = 60

        for i in range(sleep_time.minute, wake_time):
            guard_sleeps[active_guard][i] += 1
        
        sleep_time = False        

    if current_event.action == 'new shift':
        active_guard = current_event.guard

    if current_event.action == 'sleep':
        sleep_time = current_event.time

most_asleep_guard = max(guard_sleeps, key= lambda x: sum(guard_sleeps[x]))
minute_most_asleep = guard_sleeps[most_asleep_guard].index(max(guard_sleeps[most_asleep_guard]))

print(most_asleep_guard*minute_most_asleep)
