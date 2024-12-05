use std::{fs,env};
use aoc_2024::run_day;

fn main() {
    let args: Vec<String> = env::args().collect();
    
    if args.len() < 3 {
        eprintln!("Too few arguments. Usage: cargo run day part (optionally -t for test-data)");
        return;
    }

    let day: usize = args[1].parse().expect("Day must be a number");
    let part: usize = args[2].parse().expect("Part must be a number");
    
    let file_path = match args.get(3) {
        Some(t) if t == "-t" => format!("../inputs/{day}-test-{part}"),
        None => format!("../inputs/{day}-input"),
        _ => { eprintln!("Only valid flag is -t for running against test data. by default input data is use"); return;}
      };
    
    let input = fs::read_to_string(file_path);

    match input {
        Ok(input) => run_day(day,part,input),
        Err(e) => panic!("{e}"),
    };
}
