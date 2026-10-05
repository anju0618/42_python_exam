def schedule_meetings(intervals: list[tuple[int, int]]) -> tuple[int, list]:


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('three meetings, two rooms', schedule_meetings([(0, 30), (5, 10), (15, 20)]), (2, [[(0, 30)], [(5, 10), (15, 20)]]))
    check('empty list', schedule_meetings([]), (0, []))
    check('single meeting', schedule_meetings([(1, 5)]), (1, [[(1, 5)]]))
    check('no overlap', schedule_meetings([(1, 2), (3, 4), (5, 6)]), (1, [[(1, 2), (3, 4), (5, 6)]]))
    check('end == start shares room', schedule_meetings([(1, 5), (5, 10)]), (1, [[(1, 5), (5, 10)]]))
    check('all overlap', schedule_meetings([(1, 10), (2, 9), (3, 8)]), (3, [[(1, 10)], [(2, 9)], [(3, 8)]]))
    check('unsorted input', schedule_meetings([(15, 20), (0, 30), (5, 10)]), (2, [[(0, 30)], [(5, 10), (15, 20)]]))
    check('reverse order no overlap', schedule_meetings([(5, 6), (3, 4), (1, 2)]), (1, [[(1, 2), (3, 4), (5, 6)]]))
    check('same start keeps input order', schedule_meetings([(5, 10), (5, 7), (5, 6)]), (3, [[(5, 10)], [(5, 7)], [(5, 6)]]))
    check('first free room is chosen', schedule_meetings([(0, 5), (1, 3), (6, 8)]), (2, [[(0, 5), (6, 8)], [(1, 3)]]))
    check('later room reused', schedule_meetings([(0, 10), (1, 3), (4, 6), (7, 9)]), (2, [[(0, 10)], [(1, 3), (4, 6), (7, 9)]]))
    check('two rooms both free -> first', schedule_meetings([(0, 2), (1, 3), (4, 5)]), (2, [[(0, 2), (4, 5)], [(1, 3)]]))
    check('third room needed', schedule_meetings([(0, 4), (1, 5), (2, 6), (4, 7)]), (3, [[(0, 4), (4, 7)], [(1, 5)], [(2, 6)]]))
    check('zero-length meeting', schedule_meetings([(3, 3), (3, 5)]), (1, [[(3, 3), (3, 5)]]))
    check('unsorted, chain in one room', schedule_meetings([(9, 10), (1, 4), (2, 3), (4, 9)]), (2, [[(1, 4), (4, 9), (9, 10)], [(2, 3)]]))
