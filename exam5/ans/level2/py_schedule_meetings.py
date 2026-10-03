def schedule_meetings(intervals: list[tuple[int, int]]) -> tuple[int, list]:
    if not intervals:
        return (0, [])

    ordered = list(intervals)
    for i in range(1, len(ordered)):
        key = ordered[i]
        j = i - 1
        while j >= 0 and ordered[j][0] > key[0]:
            ordered[j + 1] = ordered[j]
            j -= 1
        ordered[j + 1] = key

    rooms = []
    for meeting in ordered:
        start, _ = meeting
        assigned = False
        for room in rooms:
            if room[-1][1] <= start:
                room.append(meeting)
                assigned = True
                break
        if not assigned:
            rooms.append([meeting])

    return (len(rooms), rooms)
