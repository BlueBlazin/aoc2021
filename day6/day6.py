from collections import Counter, defaultdict


def part1():
    with open("./input", "r") as f:
        fish = list(map(int, f.read().split(",")))

    new_fish = []
    for _ in range(80):
        for n in fish:
            if n == 0:
                new_fish.append(6)
                new_fish.append(8)
            else:
                new_fish.append(n - 1)
        fish = new_fish
        new_fish = []

    return len(fish)


def part2():
    with open("./input", "r") as f:
        fish = Counter(map(int, f.read().split(",")))

    new_fish = defaultdict(lambda: 0)
    for _ in range(256):
        for n, c in fish.items():
            if n == 0:
                new_fish[6] += c
                new_fish[8] += c
            else:
                new_fish[n - 1] += c
        fish = new_fish
        new_fish = defaultdict(lambda: 0)

    return sum(fish.values())


if __name__ == "__main__":
    print(part1())
    print(part2())
