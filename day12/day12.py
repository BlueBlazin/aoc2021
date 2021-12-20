from collections import defaultdict


def part1():
    g = defaultdict(set)
    size = {}

    with open("input", "r") as f:
        for line in f:
            u, v = line.strip().split("-")
            g[u].add(v)
            g[v].add(u)
            if u not in size:
                size[u] = "small" if "a" <= u[0] <= "z" else "large"
            if v not in size:
                size[v] = "small" if "a" <= v[0] <= "z" else "large"

    seen = {u: False for u in size}

    def dfs(u):
        if u == "end":
            return 1

        paths = 0
        if size[u] == "small":
            seen[u] = True

        for v in g[u]:
            if seen[v]:
                continue
            paths += dfs(v)

        seen[u] = False
        return paths

    return dfs("start")


def part2():
    g = defaultdict(set)
    size = {}

    with open("input", "r") as f:
        for line in f:
            u, v = line.strip().split("-")
            if u != "end":
                g[u].add(v)
            if u != "start" and v != "end":
                g[v].add(u)
            if u not in size:
                size[u] = "small" if "a" <= u[0] <= "z" else "large"
            if v not in size:
                size[v] = "small" if "a" <= v[0] <= "z" else "large"

    paths = set()

    def dfs(u, x, seen_count, p):
        if u == "end":
            paths.add(p + "end")
            return

        if size[u] == "small":
            seen_count[u] += 1

        p = f"{p}{u}-"

        for v in g[u]:
            if v == x:
                if seen_count[v] == 2:
                    continue
            else:
                if seen_count[v] == 1:
                    continue
            dfs(v, x, seen_count, p)

        if size[u] == "small":
            seen_count[u] -= 1

    smalls = [u for u, s in size.items() if s == "small" and u not in [
        "start", "end"]]
    for x in smalls:
        small_count = {u: 0 for u in size}
        dfs("start", x, small_count, "")
    return len(paths)


if __name__ == "__main__":
    print(part1())
    print(part2())
