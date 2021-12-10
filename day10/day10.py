import numpy as np

SCORES1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
SCORES2 = {')': 1, ']': 2, '}': 3, '>': 4}


def first_illegal(line):
    stack = []
    for c in line:
        match c:
            case '[' | '(' | '{' | '<':
                stack.append(c)
            case ']':
                if stack.pop() != '[':
                    return c
            case ')':
                if stack.pop() != '(':
                    return c
            case '}':
                if stack.pop() != '{':
                    return c
            case '>':
                if stack.pop() != '<':
                    return c


def incompletes(line):
    stack = []
    for c in line:
        match c:
            case '[' | '(' | '{' | '<':
                stack.append(c)
            case ']':
                if stack.pop() != '[':
                    return
            case ')':
                if stack.pop() != '(':
                    return
            case '}':
                if stack.pop() != '{':
                    return
            case '>':
                if stack.pop() != '<':
                    return
    return stack


def get_score(stack):
    score = 0

    while stack:
        match stack.pop():
            case '[':
                score = score * 5 + SCORES2[']']
            case '(':
                score = score * 5 + SCORES2[')']
            case '{':
                score = score * 5 + SCORES2['}']
            case '<':
                score = score * 5 + SCORES2['>']
    return score


def part1():
    with open("input", "r") as f:
        lines = f.readlines()

    ans = 0
    for line in lines:
        if (illegal := first_illegal(line.strip())) is not None:
            ans += SCORES1[illegal]
    return ans


def part2():
    with open("input", "r") as f:
        lines = f.readlines()

    scores = []

    for line in lines:
        stack = incompletes(line)
        if stack is not None:
            scores.append(get_score(stack))

    return np.median(scores)


if __name__ == "__main__":
    print(part1())
    print(part2())
