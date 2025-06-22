use std::collections::{HashMap, HashSet};

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

pub fn p2(_input: String) -> i32 {
    2
}
