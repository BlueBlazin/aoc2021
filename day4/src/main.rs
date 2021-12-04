use ndarray::prelude::*;
use std::collections::HashMap;

fn parse_board_line(
    line: &str,
    board: usize,
    row: usize,
    map: &mut HashMap<usize, Vec<(usize, usize, usize)>>,
) -> [usize; 5] {
    let nums: Vec<usize> = line
        .trim()
        .split_ascii_whitespace()
        .map(|n| n.parse().unwrap())
        .collect();

    for (col, &n) in nums.iter().enumerate() {
        let entry = map.entry(n).or_insert(vec![]);
        entry.push((board, row, col));
    }

    [nums[0], nums[1], nums[2], nums[3], nums[4]]
}

fn read_input() -> (
    Vec<usize>,
    Vec<Array2<usize>>,
    Vec<Array2<usize>>,
    HashMap<usize, Vec<(usize, usize, usize)>>,
) {
    let mut input = include_str!("../input").lines();

    let numbers: Vec<usize> = input
        .next()
        .unwrap()
        .split(",")
        .map(|n| n.parse().unwrap())
        .collect();

    let mut boards = vec![];
    let mut states = vec![];
    let mut i = 0;
    let mut map = HashMap::new();

    // skip empty line between numbers and first board
    input.next();

    loop {
        // parse 5 lines
        boards.push(array![
            parse_board_line(input.next().unwrap(), i, 0, &mut map),
            parse_board_line(input.next().unwrap(), i, 1, &mut map),
            parse_board_line(input.next().unwrap(), i, 2, &mut map),
            parse_board_line(input.next().unwrap(), i, 3, &mut map),
            parse_board_line(input.next().unwrap(), i, 4, &mut map),
        ]);

        states.push(Array::<usize, _>::zeros((5, 5).f()));

        // parse possible empty line
        if input.next().is_none() {
            break;
        }

        i += 1;
    }

    (numbers, boards, states, map)
}

fn answer(state: &Array2<usize>, board: &Array2<usize>, number: usize) -> usize {
    let mut unmarked = 0;

    for i in 0..5 {
        for j in 0..5 {
            if state[[i, j]] == 0 {
                unmarked += board[[i, j]];
            }
        }
    }

    unmarked * number
}

fn part1() -> usize {
    let (numbers, boards, mut states, map) = read_input();

    // let's play the game
    for (i, n) in numbers.into_iter().enumerate() {
        for &(board, row, col) in &map[&n] {
            states[board][[row, col]] = 1;
        }
        // skip until 5 numbers have been drawn
        if i < 4 {
            continue;
        }

        // check if any board has a bingo!
        for s in 0..states.len() {
            let state = &states[s];
            let full_row = state.sum_axis(Axis(0)).iter().any(|&n| n == 5);
            let full_col = state.sum_axis(Axis(1)).iter().any(|&n| n == 5);

            if full_row || full_col {
                return answer(state, &boards[s], n);
            }
        }
    }

    0
}

fn part2() -> usize {
    let (numbers, boards, mut states, map) = read_input();
    let mut bingo_boards = vec![false; boards.len()];
    let mut last_board = 0;
    let mut last_num = numbers[0];
    let mut num_bingo_boards = 0;

    // let's play the game
    'outer: for (i, n) in numbers.into_iter().enumerate() {
        last_num = n;

        for &(board, row, col) in &map[&n] {
            states[board][[row, col]] = 1;
        }
        // skip until 5 numbers have been drawn
        if i < 4 {
            continue;
        }

        // check if any board has a bingo!
        for s in 0..states.len() {
            if bingo_boards[s] {
                continue;
            }

            let state = &states[s];
            let full_row = state.sum_axis(Axis(0)).iter().any(|&n| n == 5);
            let full_col = state.sum_axis(Axis(1)).iter().any(|&n| n == 5);

            if full_row || full_col {
                bingo_boards[s] = true;
                last_board = s;
                num_bingo_boards += 1;

                if num_bingo_boards == boards.len() {
                    break 'outer;
                }
            }
        }
    }

    answer(&states[last_board], &boards[last_board], last_num)
}

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}
