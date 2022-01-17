from heapq import heappush, heappop


def maxEvents(events):
    events.sort()
    total_days = max(end for start, end in events)
    print(total_days)
    day = 0
    event_id = 0
    num_events_attended = 0
    min_heap = []

    for day in range(1, total_days+1):
        # Add all the events that start today
        while event_id < len(events) and events[event_id][0] == day:
            heappush(min_heap, events[event_id][1])
            event_id += 1

        # Remove all the events whose end date was before today
        while min_heap and min_heap[0] < day:
            heappop(min_heap)

        # if any event that can be attended today, let's attend it

        if min_heap:
            heappop(min_heap)
            num_events_attended += 1

    return num_events_attended


events = [[1, 2], [2, 3], [3, 4]]
print(maxEvents(events))

events = [[1, 2], [2, 3], [3, 4], [1, 2]]
print(maxEvents(events))
