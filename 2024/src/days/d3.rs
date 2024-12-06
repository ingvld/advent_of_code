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
   let re = Regex::new(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)").unwrap();
   let mut mul = true;

   re.find_iter(&input)
       .fold(0, |acc, m| acc + {
           match m.as_str() {
               "do()" => {mul = true; 0},
               "don't()" => {mul = false; 0}
               x => {
                   if !mul {0}
                   else {
                       x.split(&['(',',',')'])
                           .skip(1)
                           .take(2)
                           .map(|n| n.parse::<i32>().unwrap())
                           .product()
                   }
               }
           }
       })
}
