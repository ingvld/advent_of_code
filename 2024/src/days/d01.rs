use std::collections::{BinaryHeap, HashMap};

pub fn p1(input: String) -> i32 {
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

    diff
}

pub fn p2(input: String) -> i32 {
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
    
    left.iter().fold(0, |acc, n| acc+n*right.get(n).unwrap_or(&0))
}


