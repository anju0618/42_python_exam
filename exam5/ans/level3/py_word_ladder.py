def word_ladder(start: str, end: str, sentence: list[str]) -> int:
    if end not in sentence:
        return 0

    visited = {start: True}
    queue = [(start, 1)]
    idx = 0

    while idx < len(queue):
        word, length = queue[idx]
        idx += 1
        if word == end:
            return length

        for candidate in sentence:
            if candidate in visited:
                continue
            diff = 0
            for i in range(len(word)):
                if word[i] != candidate[i]:
                    diff += 1
                    if diff > 1:
                        break
            if diff == 1:
                visited[candidate] = True
                queue.append((candidate, length + 1))

    return 0
