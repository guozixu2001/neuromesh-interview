def min_subsequences(source, target):
    if any(ch not in source for ch in target):
        return -1

    result = 0
    i = 0  # iterator of source
    j = 0  # iterator of target

    while j < len(target):
        found = False
        while i < len(source):
            if source[i] == target[j]:
                j += 1
                found = True
                if j == len(target):
                    return result + 1
            i += 1

        if not found:
            return -1

        result += 1
        i = 0

    return result


test_cases = [
    ("abc", "abcbc", 2),
    ("abc", "acdbc", -1),
    ("xyz", "xzyxz", 3),
    ("aa", "aaaa", 2),
    ("abcd", "dcba", 4),
    ("", "a", -1),
    ("abc", "", 0),
    ("!@#", "!@#@!", 3),
    ("abcdefghijklmnopqrstuvwxyz", "pakjgb", 5),
    ("abcdefgh", "abcd", 1),
    ("abcabcabc", "abc", 1),
    ("a", "aaaaaaaaaa", 10),
]

for source, target, expected in test_cases:
    result = min_subsequences(source, target)
    print(f"source: '{source}', target: '{target}' -> Expected: {expected}, Got: {result}")
