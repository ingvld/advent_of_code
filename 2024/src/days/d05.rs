use std::{
    cmp::Ordering,
    collections::{HashMap, HashSet},
};

use itertools::Itertools;

pub fn p1(input: String) -> i32 {
    let (rules, updates) = input.split_once("\n\n").unwrap();

    let mut rulemap: HashMap<&str, HashSet<&str>> = HashMap::new();

    for rule in rules.lines() {
        let (v, k) = rule.split_once("|").unwrap();
        rulemap.entry(k).or_insert(HashSet::new()).insert(v);
    }

    let mut sum = 0;

    for update in updates.lines().map(|l| l.split(',').collect::<Vec<&str>>()) {
        let mid = update[update.len() / 2].parse::<i32>().unwrap();
        let mut incl = true;

        let mut illegals: HashSet<&str> = HashSet::new();

        for x in update {
            if illegals.contains(x) {
                incl = false;
            }
            if rulemap.contains_key(x) {
                illegals.extend(rulemap.get(x).unwrap());
            }
        }

        if incl {
            sum += mid;
        }
    }

    sum
}

pub fn p2(input: String) -> i32 {
    let (rules, updates) = input.split_once("\n\n").unwrap();

    let ruleset: HashSet<(&str, &str)> = rules
        .lines()
        .map(|line| line.split_once("|").unwrap())
        .collect();

    updates
        .lines()
        .map(|l| l.split(',').collect_vec())
        .filter_map(|mut update| {
            let mut was_unsorted = false;
            update.sort_by(|&x, &y| {
                if ruleset.contains(&(x, y)) {
                    was_unsorted = true;
                    Ordering::Greater
                } else if ruleset.contains(&(y, x)) {
                    Ordering::Less
                } else {
                    Ordering::Equal
                }
            });
            was_unsorted.then_some(update)
        })
        .fold(0, |acc, u| acc + u[u.len() / 2].parse::<i32>().unwrap())
}
