use aoc_2025::run_day;
use std::{env, fs};

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() < 3 {
        eprintln!("Too few arguments. Usage: cargo run day part (optionally -t for test-data)");
        return;
    }

    let day: usize = args[1].parse().expect("Day must be a number");
    let part: usize = args[2].parse().expect("Part must be a number");

    let input = match args.get(3) {
        Some(t) if t == "-t" => {
            let solo = fs::read_to_string(format!("../inputs/{day}-test-{part}"));
            match solo {
                Ok(_) => solo,
                Err(_) => fs::read_to_string(format!("../inputs/{day}-test")),
            }
        }
        None => fs::read_to_string(format!("../inputs/{day}-input")),
        _ => {
            eprintln!("Only valid flag is -t for running against test data. by default full input data is used");
            return;
        }
    };

    match input {
        Ok(input) => run_day(day, part, input),
        Err(e) => panic!("{e}"),
    };
}
