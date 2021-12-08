from itertools import product

LEN_TO_NUMS = {
    2: {1},
    3: {7},
    4: {4},
    5: {5, 2, 3},
    6: {0, 6, 9},
    7: {8},
}


NUM_TO_LETTERS = {
    0: set('abcefg'),
    1: set('cf'),
    2: set('acdeg'),
    3: set('acdfg'),
    4: set('bcdf'),
    5: set('abdfg'),
    6: set('abdefg'),
    7: set('acf'),
    8: set('abcdefg'),
    9: set('abcdfg'),
}

LETTERS_TO_NUMS = {"".join(sorted(v)): str(k)
                   for k, v in NUM_TO_LETTERS.items()}


def part1():
    with open('input', 'r') as f:
        lines = f.readlines()
        lines = [line.split(" | ") for line in lines]
        lines = [(line[0].split(), line[1].split()) for line in lines]

    num_uniques = 0
    for _, right in lines:
        for num in right:
            if len(LEN_TO_NUMS[len(num)]) == 1:
                num_uniques += 1

    return num_uniques


def decode(left, right):
    letters_to_vals = {c: set('abcdefg') for c in 'abcdefg'}
    left = list(map(set, left))
    for (w1, w2) in product(left, left):
        d1 = w1 - w2
        if len(d1) == 0:
            continue
        for c in d1:
            vals = letters_to_vals[c]
            res = set()

            nums1, nums2 = LEN_TO_NUMS[len(w1)], LEN_TO_NUMS[len(w2)]
            for n1 in nums1:
                for n2 in nums2:
                    d2 = NUM_TO_LETTERS[n1] - NUM_TO_LETTERS[n2]
                    if len(d2) == 0:
                        continue
                    res |= vals & d2
            letters_to_vals[c] = res

    used = {list(c)[0] for c in letters_to_vals.values() if len(c) == 1}
    for c, vals in letters_to_vals.items():
        if len(vals) == 1:
            continue
        new_vals = {v for v in vals if v not in used}
        letters_to_vals[c] = new_vals
    mapping = {c: list(v)[0] for c, v in letters_to_vals.items()}
    right = ["".join(sorted(map(mapping.get, w))) for w in right]
    return int("".join(map(LETTERS_TO_NUMS.get, right)))


def part2():
    with open('input', 'r') as f:
        lines = f.readlines()
        lines = [line.split(" | ") for line in lines]
        lines = [(line[0].split(), line[1].split()) for line in lines]

    ans = 0

    for left, right in lines:
        ans += decode(left, right)

    return ans


if __name__ == "__main__":
    print(part1())
    print(part2())
