use std::process;

pub mod days;

pub fn run_day(day: usize, part: usize, input: String) {
    let result = match (day,part) {
        (1,1) => days::d1::p1(input),
        (1,2) => days::d1::p2(input),
        (2,1) => days::d2::p1(input),
        (2,2) => days::d2::p2(input),
        (3,1) => days::d3::p1(input),
        (3,2) => days::d3::p2(input),
        _ => { eprintln!("Day {day} part {part} not available"); process::exit(1); }
    };

    println!("D{day}P{part}: {result}");
}
