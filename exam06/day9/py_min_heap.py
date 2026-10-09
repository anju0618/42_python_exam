"""py_min_heap  (問題文: py_min_heap.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


class MinHeap:
    def __init__(self):
        pass

    def push(self, x) -> None:
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    def size(self) -> int:
        pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    h = MinHeap()
    check('new heap size', h.size(), 0)
    check('pop on empty', h.pop(), None)
    for x in [5, 3, 8, 1]:
        h.push(x)
    check('peek', h.peek(), 1)
    check('pop 1', h.pop(), 1)
    check('pop 3', h.pop(), 3)
    check('size 2', h.size(), 2)
    h.push(0)
    check('pop 0', h.pop(), 0)
    check('pop 5', h.pop(), 5)
    check('pop 8', h.pop(), 8)
    check('empty again', h.size(), 0)
    h = MinHeap()
    vals = [(i * 7919) % 2003 for i in range(2000)]
    for v in vals:
        h.push(v)
    out = [h.pop() for _ in range(len(vals))]
    check('2000 random values come out sorted', out == sorted(vals), True)
    h = MinHeap()
    for x in [2, 2, 1, 1]:
        h.push(x)
    check('duplicates', [h.pop() for _ in range(4)], [1, 1, 2, 2])
