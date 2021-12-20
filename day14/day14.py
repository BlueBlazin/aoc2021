from collections import Counter, defaultdict


def process(template, rules):
    new_template = ""
    for i in range(len(template) - 1):
        first, second = template[i], template[i + 1]
        if (first, second) in rules:
            new_template += f"{first}{rules[first, second]}"
        else:
            new_template += first
    new_template += template[-1]
    return new_template


def part1():
    with open("input", "r") as f:
        template = f.readline().strip()
        f.readline()  # skip empty line

        rules = {}
        for line in f:
            line = line.strip()
            left, right = line.split(" -> ")
            rules[tuple(left)] = right

    for _ in range(10):
        template = process(template, rules)

    counts = Counter(template)
    return (max(counts.values()) - min(counts.values()))


def part2():
    with open("input", "r") as f:
        template = f.readline().strip()
        f.readline()  # skip empty line

        rules = {}
        for line in f:
            line = line.strip()
            left, right = line.split(" -> ")
            rules[left] = right

    pairs = defaultdict(lambda: 0)
    for a, b in zip(template, template[1:]):
        pairs[f"{a}{b}"] += 1

    for _ in range(40):
        new_pairs = defaultdict(lambda: 0)

        for pair, count in pairs.items():
            if pair in rules:
                start, middle, end = pair[0], rules[pair], pair[1]
                new_pairs[f"{start}{middle}"] += count
                new_pairs[f"{middle}{end}"] += count
            else:
                new_pairs[pair] += count
        pairs = new_pairs

    counts = defaultdict(lambda: 0)
    counts[template[0]] += 1
    counts[template[-1]] += 1

    for pair, count in pairs.items():
        counts[pair[0]] += count
        counts[pair[1]] += count

    return (max(counts.values()) - min(counts.values())) // 2


if __name__ == "__main__":
    print(part1())
    print(part2())
