pub fn p1(input : String) -> i32 {
    let input_chars : Vec<Vec<char>> = input
        .lines()
        .map(|line| line.chars().collect::<Vec<char>>())
        .collect();
    
    for i in 0..input_chars.len() {
        for j in 1..input_chars[0].len() {
            if input_chars[i][j] == 'X' {
                println!("{i} {j}");
            }
        }
      
    }


    1
}

pub fn p2(_input : String) -> i32 {
    2
}

/*  M       A       S
 *   0 +1    0 +2    0 +3
 *  +1 +1   +2 +2   +3 +3
 *  +1  0   +2  0   +3  0
 *  +1 -1   +2 -2   +3 -3
 *   0 -1    0 -2    0 -3
 *  -1 -1   -2 -2   -3 -3
 *  -1  0   -2  0   -3  0
 *  -1 +1   -2 +2   -3 +3
 */
