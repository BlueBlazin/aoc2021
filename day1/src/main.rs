fn part1() -> usize {
    let values: Vec<usize> = include_str!("../input")
        .lines()
        .map(|n| n.parse().unwrap())
        .collect();

    let mut count = 0;

    for i in 1..values.len() {
        if values[i - 1] < values[i] {
            count += 1;
        }
    }

    count
}

fn part2() -> usize {
    let values: Vec<usize> = include_str!("../input")
        .lines()
        .map(|n| n.parse().unwrap())
        .collect();

    let mut count = 0;
    let mut curr: usize = values[..3].iter().sum();

    for i in 3..values.len() {
        let new = curr - values[i - 3] + values[i];
        if new > curr {
            count += 1;
        }
        curr = new;
    }

    count
}

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}
