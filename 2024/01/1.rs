use std::collections::{BinaryHeap, HashMap};
use std::{env,fs};

fn p1(input: &str) {
    let mut left_heap = BinaryHeap::new();
    let mut right_heap = BinaryHeap::new();

    let split = input.split_whitespace().filter_map(|n| n.parse::<i32>().ok());
    
    for (i, n) in split.enumerate() {
        match i%2 {
            0 => left_heap.push(n),
            1 => right_heap.push(n),
            _ => unreachable!(),
        };
    }

    let mut diff = 0;

    while let (Some(left), Some(right)) = (left_heap.pop(), right_heap.pop()) {
        diff += (left-right).abs();
    }

    println!("Result p1: {diff}");
}

fn p2(input: &str) {
    let mut left = Vec::new(); 
    let mut right = HashMap::new();

    let split = input.split_whitespace().filter_map(|n| n.parse::<i32>().ok());

    for (i, n) in split.enumerate() {
        if i%2 == 0 {
            left.push(n);
        } else {
            *right.entry(n).or_insert(0) += 1;
        }
    }
    
    let result = left.iter().fold(0, |acc, n| acc+n*right.get(n).unwrap_or(&0));
    println!("Results p2: {result}")
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let file_name = args.get(1)
        .expect("No file name passed");
    let input = fs::read_to_string(file_name)
        .expect("Failed to read file");
    p2(&input);

}
