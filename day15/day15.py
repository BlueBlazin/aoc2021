import networkx as nx
from networkx.algorithms.shortest_paths.weighted import dijkstra_path_length


def part1():
    with open("input", "r") as f:
        grid = f.readlines()
        grid = [list(map(int, line.strip())) for line in grid]

    DG = nx.DiGraph()

    for i in range(100):
        for j in range(100):
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ip, jp = i + di, j + dj
                if 0 <= ip <= 99 and 0 <= jp <= 99:
                    DG.add_edge((i, j), (ip, jp), weight=grid[ip][jp])

    return dijkstra_path_length(DG, (0, 0), (99, 99))


def part2():
    grid = [[0] * 500 for _ in range(500)]

    with open("input", "r") as f:
        for i, line in enumerate(f.readlines()):
            for j, v in enumerate(line.strip()):
                grid[i][j] = int(v)

    for i in range(100, 500):
        for j in range(100):
            grid[i][j] = max(1, (grid[i - 100][j] + 1) % 10)

    for i in range(0, 500):
        for j in range(100, 500):
            grid[i][j] = max(1, (grid[i][j - 100] + 1) % 10)

    DG = nx.DiGraph()

    for i in range(len(grid)):
        for j in range(len(grid)):
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ip, jp = i + di, j + dj
                if 0 <= ip < len(grid) and 0 <= jp < len(grid):
                    DG.add_edge((i, j), (ip, jp), weight=grid[ip][jp])

    return dijkstra_path_length(DG, (0, 0), (len(grid) - 1, len(grid) - 1))


if __name__ == "__main__":
    print(part1())
    print(part2())
