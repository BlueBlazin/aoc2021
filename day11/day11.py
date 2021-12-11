import numpy as np
from itertools import product


def flash(grid, i, j, t, flashed):
    if grid[i, j] == 10:
        grid[i, j] = 0
        flashed[t].add((i, j))
        boost_neighbors(grid, i, j, t, flashed)


def boost_neighbors(grid, i, j, t, flashed):
    for di, dj in [(1, 0), (0, 1), (1, 1), (1, -1)]:
        ip, jp = i + di, j + dj
        if 0 <= ip < 10 and 0 <= jp < 10:
            if (ip, jp) not in flashed[t]:
                grid[ip, jp] += 1
                flash(grid, ip, jp, t, flashed)

        ip, jp = i - di, j - dj
        if 0 <= ip < 10 and 0 <= jp < 10:
            if (ip, jp) not in flashed[t]:
                grid[ip, jp] += 1
                flash(grid, ip, jp, t, flashed)


def part1():
    with open("input", "r") as f:
        grid = [list(map(int, line.strip())) for line in f.readlines()]

    grid = np.array(grid)
    flashed = {}

    for t in range(100):
        flashed[t] = set()
        for i, j in product(range(10), range(10)):
            if (i, j) not in flashed[t]:
                grid[i, j] += 1
                flash(grid, i, j, t, flashed)

    return sum(len(x) for x in flashed.values())


def part2():
    with open("input", "r") as f:
        grid = [list(map(int, line.strip())) for line in f.readlines()]

    t = 1
    grid = np.array(grid)
    flashed = {}

    while True:
        flashed[t] = set()
        for i, j in product(range(10), range(10)):
            if (i, j) not in flashed[t]:
                grid[i, j] += 1
                flash(grid, i, j, t, flashed)

        if len(flashed[t]) == 100:
            return t
        t += 1


if __name__ == "__main__":
    print(part1())
    print(part2())
