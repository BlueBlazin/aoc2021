import numpy as np
from collections import Counter
from functools import reduce


def part1():
    grid = []

    with open("input", "r") as f:
        for line in f:
            grid.append(list(map(int, line.strip())))

    grid = np.array(grid)
    height, width = grid.shape

    ans = 0
    for i in range(height):
        for j in range(width):
            top = i > 0 and grid[i, j] < grid[i - 1, j]
            bottom = i < height - 1 and grid[i, j] < grid[i + 1, j]
            left = j > 0 and grid[i, j] < grid[i, j - 1]
            right = j < width - 1 and grid[i, j] < grid[i, j + 1]
            if all((i <= 0 or top,
                    i >= height - 1 or bottom,
                    j <= 0 or left,
                    j >= width - 1 or right)):
                ans += (grid[i, j] + 1)
    return ans


def part2():
    grid = []

    with open("input", "r") as f:
        for line in f:
            grid.append(list(map(int, line.strip())))

    grid = np.array(grid)
    height, width = grid.shape
    basins = []

    for i in range(height):
        for j in range(width):
            top = i > 0 and grid[i, j] < grid[i - 1, j]
            bottom = i < height - 1 and grid[i, j] < grid[i + 1, j]
            left = j > 0 and grid[i, j] < grid[i, j - 1]
            right = j < width - 1 and grid[i, j] < grid[i, j + 1]
            if all((i <= 0 or top,
                    i >= height - 1 or bottom,
                    j <= 0 or left,
                    j >= width - 1 or right)):
                basins.append((i, j))

    seen = np.full_like(grid, fill_value=-1)
    cc = 0
    counts = Counter()

    def dfs(i, j):
        neighbors = []

        if i > 0 and grid[i, j] > grid[i - 1, j]:
            neighbors.append((grid[i - 1, j], i - 1, j))
        if i < height - 1 and grid[i, j] > grid[i + 1, j]:
            neighbors.append((grid[i + 1, j], i + 1, j))
        if j > 0 and grid[i, j] > grid[i, j - 1]:
            neighbors.append((grid[i, j - 1], i, j - 1))
        if j < width - 1 and grid[i, j] > grid[i, j + 1]:
            neighbors.append((grid[i, j + 1], i, j + 1))

        if len(neighbors) > 0:
            _, ni, nj = min(neighbors)
            if seen[ni, nj] != -1:
                seen[i, j] = seen[ni, nj]
            else:
                seen[i, j] = dfs(ni, nj)
        else:
            seen[i, j] = cc
        return seen[i, j]

    for i in range(height):
        for j in range(width):
            cc += 1
            if seen[i, j] != -1 or grid[i, j] == 9:
                continue
            dfs(i, j)

    for i in range(height):
        for j in range(width):
            counts[seen[i, j]] += 1

    counts[-1] = 0
    return reduce(lambda a, x: a * x[1], counts.most_common(3), 1)


if __name__ == "__main__":
    print(part1())
    print(part2())
