"""py_cheapest_flight  (問題文: py_cheapest_flight.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def cheapest_flight(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', cheapest_flight(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1), 700)
    check('example 2', cheapest_flight(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1), 200)
    check('example 3 (k=0)', cheapest_flight(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0), 500)
    check('unreachable', cheapest_flight(3, [[0, 1, 1]], 0, 2, 5), -1)
    check('src = dst', cheapest_flight(2, [], 0, 0, 0), 0)
    check('too many stops needed', cheapest_flight(4, [[0, 1, 1], [1, 2, 1], [2, 3, 1]], 0, 3, 1), -1)
    check('exactly enough stops', cheapest_flight(4, [[0, 1, 1], [1, 2, 1], [2, 3, 1]], 0, 3, 2), 3)
