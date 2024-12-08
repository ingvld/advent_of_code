use itertools::Itertools;

pub fn p1(input: String) -> i32 {
    input
        .lines()
        .map( |r| 
            r.split(" ")
            .filter_map( |n| n.parse::<i32>().ok()))
        .fold( 0, |acc, r| acc +
            match match r.clone().take(2).collect_tuple().unwrap() {
                (a,b) if a < b => r.is_sorted_by(|x,y| x < y && 1 <= y-x && y-x <= 3),
                _ => r.is_sorted_by(|x,y| x > y && 1 <= x-y && x-y <= 3),
            } {
                true => 1,
                false => 0,
            },
            )
}

pub fn p2(input: String) -> i32 {
    let reports = input.lines().map( |r| r.split(" ").filter_map( |n| n.parse::<i32>().ok()).collect::<Vec<i32>>());
    
    for report in reports {
        let r = report.windows(2).map(|pair| pair[0]-pair[1]);
        for x in r {
            dbg!(x);
        } 
    }

    0
}

