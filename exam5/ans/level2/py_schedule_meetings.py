def schedule_meetings(intervals: list[tuple[int, int]]) -> tuple[int, list]:
    ordered = []
    for m in intervals:
        i = 0
        while i < len(ordered) and ordered[i][0] <= m[0]:
            i += 1
        ordered.insert(i, m)

    rooms = []
    for m in ordered:
        for room in rooms:
            if room[-1][1] <= m[0]:
                room.append(m)
                break
        else:
            rooms.append([m])
    return (len(rooms), rooms)
