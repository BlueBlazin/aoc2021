fn part1() -> usize {
    let inputs: Vec<(&str, usize)> = include_str!("../input")
        .lines()
        .map(|line| line.split(" ").collect::<Vec<_>>())
        .map(|x| (x[0], x[1].parse().unwrap()))
        .collect();

    let mut forward = 0;
    let mut down = 0;

    for (c, x) in inputs {
        match c {
            "up" => down -= x,
            "down" => down += x,
            "forward" => forward += x,
            _ => unreachable!(),
        }
    }

    forward * down
}

fn part2() -> usize {
    let inputs: Vec<(&str, usize)> = include_str!("../input")
        .lines()
        .map(|line| line.split(" ").collect::<Vec<_>>())
        .map(|x| (x[0], x[1].parse().unwrap()))
        .collect();

    let mut forward = 0;
    let mut down = 0;
    let mut aim = 0;

    for (c, x) in inputs {
        match c {
            "forward" => {
                forward += x;
                down += aim * x;
            }
            "down" => aim += x,
            "up" => aim -= x,
            _ => unreachable!(),
        }
    }

    forward * down
}

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}
