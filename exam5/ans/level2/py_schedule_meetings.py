def schedule_meetings(intervals: list[tuple[int, int]]) -> tuple[int, list]:
    ordered = []
    for m in intervals:
        ordered.append(m)
    n = len(ordered)
    for _ in range(n):
        for j in range(n - 1):
            if ordered[j][0] > ordered[j + 1][0]:
                ordered[j], ordered[j + 1] = ordered[j + 1], ordered[j]

    rooms = []
    for m in ordered:
        for room in rooms:
            if room[-1][1] <= m[0]:
                room.append(m)
                break
        else:
            rooms.append([m])
    return (len(rooms), rooms)
