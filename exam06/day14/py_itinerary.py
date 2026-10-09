"""py_itinerary  (問題文: py_itinerary.txt)

制約: sorted(), .sort(), set(), heapq, Counter, deque は使わない。
"""


def itinerary(tickets: list[list[str]]) -> list[str]:
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('example 1', itinerary([['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SJC'], ['LHR', 'SFO']]), ['JFK', 'MUC', 'LHR', 'SFO', 'SJC'])
    check('example 2', itinerary([['JFK', 'SFO'], ['JFK', 'ATL'], ['SFO', 'ATL'], ['ATL', 'JFK'], ['ATL', 'SFO']]), ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO'])
    check('one ticket', itinerary([['JFK', 'A']]), ['JFK', 'A'])
    check('dead end last', itinerary([['JFK', 'KUL'], ['JFK', 'NRT'], ['NRT', 'JFK']]), ['JFK', 'NRT', 'JFK', 'KUL'])
