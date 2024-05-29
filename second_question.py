def check_brackets(line):
    unmatched_left = 0
    unmatched_left_positions = []
    unmatched_right_positions = []

    for i, char in enumerate(line):
        if char == "(":
            unmatched_left_positions.append(i)
            unmatched_left += 1
        elif char == ")":
            if unmatched_left > 0:
                unmatched_left -= 1
                unmatched_left_positions.pop()
            else:
                unmatched_right_positions.append(i)

    error_line = [" "] * len(line)
    if unmatched_right_positions:
        for pos in unmatched_right_positions:
            error_line[pos] = "?"
    if unmatched_left_positions:
        for pos in unmatched_left_positions:
            error_line[pos] = "x"

    return "".join(error_line)


test_cases = ["bge)))))))))", "((IIII)))))", "()()()()(uuu", "))))UUUU((()"]
for input in test_cases:
    print(input)
    output = check_brackets(input)
    print(output)
