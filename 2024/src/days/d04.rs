use itertools::Itertools;

pub fn p1(input: String) -> i32 {
    let input_chars: Vec<Vec<char>> = input
        .lines()
        .map(|line| line.chars().collect::<Vec<char>>())
        .collect();

    let directions: Vec<(i32, i32, i32)> = vec![(1, 2, 3), (0, 0, 0), (-1, -2, -3)];

    let x_length = input_chars.len() as i32;
    let y_length = input_chars[0].len() as i32;

    (0..x_length)
        .cartesian_product(0..y_length)
        .filter(|(i, j)| input_chars[*i as usize][*j as usize] == 'X')
        .fold(0, |acc, (i, j)| {
            acc + {
                directions
                    .iter()
                    .cartesian_product(directions.clone())
                    .map(|(x, y)| ((i + x.0, i + x.1, i + x.2), (j + y.0, j + y.1, j + y.2)))
                    .filter(|(x, y)| {
                        0 <= x.0
                            && x.0 < x_length
                            && 0 <= x.1
                            && x.1 < x_length
                            && 0 <= x.2
                            && x.2 < x_length
                            && 0 <= y.0
                            && y.0 < y_length
                            && 0 <= y.1
                            && y.1 < y_length
                            && 0 <= y.2
                            && y.2 < y_length
                    })
                    .fold(0, |acc, (x, y)| {
                        acc + {
                            match (
                                input_chars[x.0 as usize][y.0 as usize],
                                input_chars[x.1 as usize][y.1 as usize],
                                input_chars[x.2 as usize][y.2 as usize],
                            ) {
                                ('M', 'A', 'S') => 1,
                                _ => 0,
                            }
                        }
                    })
            }
        })
}

pub fn p2(input: String) -> i32 {
    let input_chars: Vec<Vec<char>> = input
        .lines()
        .map(|line| line.chars().collect::<Vec<char>>())
        .collect();

    let x_length = input_chars.len();
    let y_length = input_chars[0].len();

    (1..x_length - 1)
        .cartesian_product(1..y_length - 1)
        .filter(|(i, j)| input_chars[*i][*j] == 'A')
        .fold(0, |acc, (i, j)| {
            acc + match (
                input_chars[i - 1][j - 1],
                input_chars[i + 1][j + 1],
                input_chars[i - 1][j + 1],
                input_chars[i + 1][j - 1],
            ) {
                ('M', 'S', 'M', 'S') => 1,
                ('S', 'M', 'S', 'M') => 1,
                ('M', 'S', 'S', 'M') => 1,
                ('S', 'M', 'M', 'S') => 1,
                _ => 0,
            }
        })
}
