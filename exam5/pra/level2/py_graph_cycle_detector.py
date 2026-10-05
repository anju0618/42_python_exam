def py_graph_cycle_detector(graph: dict[int, list[int]]) -> bool:


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check('cycle present', py_graph_cycle_detector({0: [1], 1: [2], 2: [0]}), True)
    check('no cycle', py_graph_cycle_detector({0: [1], 1: [2], 2: []}), False)
    check('empty graph', py_graph_cycle_detector({}), False)
    check('single node no edge', py_graph_cycle_detector({0: []}), False)
    check('self loop', py_graph_cycle_detector({0: [0]}), True)
    check('two node cycle', py_graph_cycle_detector({0: [1], 1: [0]}), True)
    check('diamond (no cycle)', py_graph_cycle_detector({0: [1, 2], 1: [3], 2: [3], 3: []}), False)
    check('diamond + back edge', py_graph_cycle_detector({0: [1, 2], 1: [3], 2: [3], 3: [0]}), True)
    check('cycle in 2nd component', py_graph_cycle_detector({0: [1], 1: [], 2: [3], 3: [2]}), True)
    check('two components no cycle', py_graph_cycle_detector({0: [1], 1: [], 2: [3], 3: []}), False)
    check('neighbor not a key', py_graph_cycle_detector({0: [1]}), False)
    check('cycle not including start', py_graph_cycle_detector({0: [1], 1: [2], 2: [3], 3: [1]}), True)
    check('long chain no cycle', py_graph_cycle_detector({0: [1], 1: [2], 2: [3], 3: [4], 4: [5], 5: []}), False)
    check('long chain back to start', py_graph_cycle_detector({0: [1], 1: [2], 2: [3], 3: [4], 4: [5], 5: [0]}), True)
    check('shared node visited twice (no cycle)', py_graph_cycle_detector({0: [2], 1: [2], 2: []}), False)
    check('keys in reverse order', py_graph_cycle_detector({3: [2], 2: [1], 1: [0], 0: []}), False)
    check('self loop deep inside', py_graph_cycle_detector({0: [1], 1: [2], 2: [2]}), True)
    check('many edges no cycle', py_graph_cycle_detector({0: [1, 2, 3], 1: [2, 3], 2: [3], 3: []}), False)
