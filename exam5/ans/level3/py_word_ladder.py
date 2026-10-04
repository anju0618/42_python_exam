def word_ladder(start: str, end: str, sentence: list[str]) -> int:
    if end not in sentence:
        return 0

    visited = {start: True}
    queue = [(start, 1)]

    for word, length in queue:
        if word == end:
            return length
        for cand in sentence:
            if cand in visited:
                continue
            diff = 0
            for i in range(len(word)):
                if word[i] != cand[i]:
                    diff += 1
            if diff == 1:
                visited[cand] = True
                queue.append((cand, length + 1))

    return 0
