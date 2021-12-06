from collections import defaultdict


def part1():
    lines = []
    with open("./input", "r") as f:
        for line in f:
            start, end = line.split(" -> ")
            x1, y1 = start.split(",")
            x2, y2 = end.split(",")
            lines.append(((int(x1), int(y1)), (int(x2), int(y2))))

    counts = defaultdict(lambda: 0)
    candidates = set()

    for (x1, y1), (x2, y2) in lines:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                counts[x1, y] += 1
                if counts[x1, y] >= 2:
                    candidates.add((x1, y))
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                counts[x, y1] += 1
                if counts[x, y1] >= 2:
                    candidates.add((x, y1))

    return len(candidates)


def part2():
    lines = []
    with open("./input", "r") as f:
        for line in f:
            start, end = line.split(" -> ")
            x1, y1 = start.split(",")
            x2, y2 = end.split(",")
            lines.append(((int(x1), int(y1)), (int(x2), int(y2))))

    counts = defaultdict(lambda: 0)
    candidates = set()

    for (x1, y1), (x2, y2) in lines:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                counts[x1, y] += 1
                if counts[x1, y] >= 2:
                    candidates.add((x1, y))
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                counts[x, y1] += 1
                if counts[x, y1] >= 2:
                    candidates.add((x, y1))
        else:
            dx = 2 * (x1 <= x2) - 1
            dy = 2 * (y1 <= y2) - 1
            for _ in range(abs(x1 - x2) + 1):
                counts[x1, y1] += 1
                if counts[x1, y1] >= 2:
                    candidates.add((x1, y1))
                x1 += dx
                y1 += dy

    return len(candidates)


if __name__ == "__main__":
    print(part1())
    print(part2())
