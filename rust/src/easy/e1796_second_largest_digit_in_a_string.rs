struct Solution;

impl Solution {
    pub fn second_highest(s: String) -> i32 {
        let mut first = -1;
        let mut second = -1;
        for c in s.chars() {
            if c.is_numeric() {
                let current = c.to_digit(10).unwrap() as i32;
                if current == first {
                    continue;
                }
                if current > first {
                    second = first;
                    first = current;
                } else if current > second {
                    second = current;
                }
            }
        }
        second
    }
}

#[test]
fn test_second_highest() {
    assert_eq!(2, Solution::second_highest("dfa12321afd".to_string()));
    assert_eq!(-1, Solution::second_highest("abc1111".to_string()));
}
