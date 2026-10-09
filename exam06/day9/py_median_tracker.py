"""py_median_tracker  (問題文: py_median_tracker.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


class MedianTracker:
    def __init__(self):
        pass

    def add(self, num: int) -> None:
        pass

    def median(self) -> float:
        pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    m = MedianTracker()
    m.add(5)
    check('one value', m.median(), 5)
    m.add(15)
    check('two values', m.median(), 10)
    m.add(1)
    check('three values', m.median(), 5)
    m.add(3)
    check('four values', m.median(), 4)
    m = MedianTracker()
    for x in range(1, 1001):
        m.add(x)
    check('1..1000', m.median(), 500.5)
    m = MedianTracker()
    for x in range(1000, 0, -1):
        m.add(x)
    check('1000..1 (reverse)', m.median(), 500.5)
    m = MedianTracker()
    m.add(-1)
    m.add(-2)
    check('negatives', m.median(), -1.5)
    m = MedianTracker()
    m.add(2)
    m.add(2)
    m.add(2)
    check('duplicates', m.median(), 2)
