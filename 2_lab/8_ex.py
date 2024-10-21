from datetime import datetime
from memory_profiler import profile


times = [
    "6",
    "09:00 10:07",
    "10:20 11:35",
    "12:00 17:00",
    "11:00 11:30",
    "11:20 12:30",
    "11:30 18:15"
]


@profile()
def calculate_visitors(data):
    N = int(data[0])
    visits = []
    for i in range(1, N+1):
        start_time, end_time = data[i].split()
        visits.append((datetime.strptime(start_time, "%H:%M"), 1))
        visits.append((datetime.strptime(end_time, "%H:%M"), -1))

    visits.sort(key=lambda x: (x[0], -x[1]))

    max_visitors = 0
    current_visitors = 0

    for _, delta in visits:
        current_visitors += delta
        max_visitors = max(max_visitors, current_visitors)

    print(max_visitors)


calculate_visitors(times)