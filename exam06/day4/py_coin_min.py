"""py_coin_min  (問題文: py_coin_min.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def coin_min(coins: list[int], amount: int) -> int:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', coin_min([1, 2, 5], 11), 3)
    check('example 2', coin_min([2], 3), -1)
    check('example 3', coin_min([1], 0), 0)
    check('greedy fails', coin_min([1, 3, 4], 6), 2)
    check('big', coin_min([186, 419, 83, 408], 6249), 20)
    check('exact one coin', coin_min([5], 5), 1)
    check('no coins', coin_min([], 5), -1)
    check('unordered', coin_min([5, 1, 2], 11), 3)
    check('only big coins', coin_min([5, 10], 3), -1)
