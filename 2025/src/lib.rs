use std::process;

pub mod days;

pub fn run_day(day: usize, part: usize, input: String) {
    let result = match (day, part) {
        (1, 1) => days::d01::p1(input),
        (1, 2) => days::d01::p2(input),
        (2, 1) => days::d02::p1(input),
        (2, 2) => days::d02::p2(input),
        (3, 1) => days::d03::p1(input),
        (3, 2) => days::d03::p2(input),
        (4, 1) => days::d04::p1(input),
        (4, 2) => days::d04::p2(input),
        (5, 1) => days::d05::p1(input),
        (5, 2) => days::d05::p2(input),
        (6, 1) => days::d06::p1(input),
        (6, 2) => days::d06::p2(input),
        (7, 1) => days::d07::p1(input),
        (7, 2) => days::d07::p2(input),
        (8, 1) => days::d08::p1(input),
        (8, 2) => days::d08::p2(input),
        (9, 1) => days::d09::p1(input),
        (9, 2) => days::d09::p2(input),
        (10, 1) => days::d10::p1(input),
        (10, 2) => days::d10::p2(input),
        (11, 1) => days::d11::p1(input),
        (11, 2) => days::d11::p2(input),
        (12, 1) => days::d12::p1(input),
        (12, 2) => days::d12::p2(input),
        _ => {
            eprintln!("Day {day} part {part} not available");
            process::exit(1);
        }
    };

    println!("D{day}P{part}: {result}");
}
