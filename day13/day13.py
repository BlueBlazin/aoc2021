import numpy as np
import matplotlib.pyplot as plt


def fold(points, coord, val):
    if coord == 'x':
        return set((x, y) if x <= val else (2 * val - x, y) for x, y in points)
    else:
        return set((x, y) if y <= val else (x, 2 * val - y) for x, y in points)


def draw(points):
    width = max(p[0] for p in points) + 1
    height = max(p[1] for p in points) + 1
    grid = [[0] * width for _ in range(height)]
    for x, y in points:
        grid[y][x] = 1
    grid = np.array(grid)
    plt.imshow(grid)
    plt.show()


def part1():
    with open("input1", "r") as f:
        points = f.readlines()
        points = [line.split(",") for line in points]
        points = [(int(x), int(y)) for x, y in points]

    with open("input2", "r") as f:
        folds = f.readlines()
        folds = [line[11:].split("=") for line in folds]
        folds = [(coord, int(val)) for coord, val in folds]

    points = fold(points, *folds[0])
    return len(points)


def part2():
    with open("input1", "r") as f:
        points = f.readlines()
        points = [line.split(",") for line in points]
        points = [(int(x), int(y)) for x, y in points]

    with open("input2", "r") as f:
        folds = f.readlines()
        folds = [line[11:].split("=") for line in folds]
        folds = [(coord, int(val)) for coord, val in folds]

    for f in folds:
        points = fold(points, *f)

    draw(points)


if __name__ == "__main__":
    print(part1())
    part2()
