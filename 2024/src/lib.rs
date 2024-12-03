use std::process;

pub mod days;

pub fn run_day(day: usize, part: usize, input: String) {
    let result = match (day,part) {
        (1,1) => days::d1::p1(input),
        (1,2) => days::d1::p2(input),
        _ => { eprintln!("Day not available: {day}. dec"); process::exit(1); }
    };

    println!("D{day}P{part}: {result}");
}
