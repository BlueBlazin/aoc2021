def part1():
    with open("input", "r") as f:
        xs = list(map(int, f.read().split(",")))

    min_fuel = float('inf')
    for a in range(min(xs), max(xs)):
        fuel = 0
        for j in range(0, len(xs)):
            fuel += abs(a - xs[j])
        min_fuel = min(min_fuel, fuel)
    return min_fuel


def part2():
    with open("input", "r") as f:
        xs = list(map(int, f.read().split(",")))

    min_fuel = float('inf')
    for a in range(min(xs), max(xs)):
        fuel = 0
        for j in range(0, len(xs)):
            n = abs(a - xs[j])
            fuel = fuel + n * (n + 1) / 2
        min_fuel = min(min_fuel, fuel)
    return min_fuel


if __name__ == "__main__":
    print(part1())
    print(part2())
