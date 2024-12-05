use regex::Regex;

pub fn p1(input : String) -> i32 {
    let re = Regex::new(r"mul\((?<n1>\d{1,3}),(?<n2>\d{1,3})\)").unwrap();
    
    re.captures_iter(&input)
        .fold(0, |acc, c| acc + 
            c.extract::<2>()
            .1
            .iter()
            .map(|x| x.parse::<i32>().unwrap())
            .product::<i32>())
}

pub fn p2(input : String) -> i32 {
    1
}
