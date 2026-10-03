def py_graph_cycle_detector(graph: dict[int, list[int]]) -> bool:


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("cycle present", py_graph_cycle_detector({0: [1], 1: [2], 2: [0]}), True)
    check("no cycle", py_graph_cycle_detector({0: [1], 1: [2], 2: []}), False)
    check("empty graph", py_graph_cycle_detector({}), False)
