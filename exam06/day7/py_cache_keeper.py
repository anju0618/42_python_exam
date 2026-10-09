"""py_cache_keeper  (問題文: py_cache_keeper.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


class CacheKeeper:
    def __init__(self, capacity: int):
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    c = CacheKeeper(2)
    c.put(1, 1)
    c.put(2, 2)
    check('get 1', c.get(1), 1)
    c.put(3, 3)
    check('2 was evicted', c.get(2), -1)
    c.put(4, 4)
    check('1 was evicted', c.get(1), -1)
    check('get 3', c.get(3), 3)
    check('get 4', c.get(4), 4)
    c = CacheKeeper(1)
    c.put(1, 1)
    c.put(1, 2)
    check('update value', c.get(1), 2)
    c.put(2, 3)
    check('capacity 1: old evicted', c.get(1), -1)
    check('capacity 1: new kept', c.get(2), 3)
    c = CacheKeeper(2)
    c.put(1, 1)
    c.put(2, 2)
    c.put(1, 10)
    c.put(3, 3)
    check('put refreshes recency (2 evicted)', c.get(2), -1)
    check('put refreshes recency (1 kept)', c.get(1), 10)
    c = CacheKeeper(2)
    c.put(1, 1)
    c.put(2, 2)
    c.get(1)
    c.put(3, 3)
    check('get refreshes recency (2 evicted)', c.get(2), -1)
    check('missing key', c.get(99), -1)
