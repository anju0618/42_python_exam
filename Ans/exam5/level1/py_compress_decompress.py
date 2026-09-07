def compress(s: str) -> str:
    if not s:
        return ""

    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1])
            if count > 1:
                result.append(str(count))
            count = 1
    result.append(s[-1])
    if count > 1:
        result.append(str(count))
    return "".join(result)


def decompress(s: str) -> str:
    result = []
    i = 0
    n = len(s)
    while i < n:
        char = s[i]
        i += 1
        digits = ""
        while i < n and s[i].isdigit():
            digits += s[i]
            i += 1
        count = int(digits) if digits else 1
        result.append(char * count)
    return "".join(result)
