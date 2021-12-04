fn part1() -> usize {
    let values: Vec<Vec<_>> = include_str!("../input")
        .lines()
        .map(|x| x.chars().map(|c| (c == '1') as usize).collect())
        .collect();

    let mut gamma = 0;
    let mut eps = 0;

    for i in 0..12 {
        let ones: usize = values.iter().map(|b| b[i]).sum();
        gamma = gamma * 2 + (ones >= values.len() / 2) as usize;
        eps = eps * 2 + (ones < values.len() / 2) as usize
    }

    gamma * eps
}

fn filter_nums<F>(mut candidates: Vec<&Vec<usize>>, pred: F) -> &Vec<usize>
where
    F: Fn(usize, usize) -> bool,
{
    let mut i = 0;

    while candidates.len() > 1 {
        let ones: usize = candidates.iter().map(|b| b[i]).sum();
        // let common = (ones >= candidates.len() / 2) as usize;
        let common = pred(ones, candidates.len() / 2) as usize;
        candidates = candidates.into_iter().filter(|b| b[i] == common).collect();
        i += 1;
    }

    candidates[0]
}

fn part2() -> usize {
    let values: Vec<Vec<_>> = include_str!("../input")
        .lines()
        .map(|x| x.chars().map(|c| (c == '1') as usize).collect())
        .collect();

    let o2 = filter_nums(values.iter().collect(), |ones, l| ones >= l);
    let co2 = filter_nums(values.iter().collect(), |ones, l| ones < l);

    let o2_val = o2.iter().fold(0, |a, &n| a * 2 + n);
    let co2_val = co2.iter().fold(0, |a, &n| a * 2 + n);

    o2_val * co2_val
}

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}
