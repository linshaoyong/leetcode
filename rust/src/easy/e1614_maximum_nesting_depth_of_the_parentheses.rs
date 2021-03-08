use std::cmp::max;

struct Solution;

impl Solution {
    pub fn max_depth(s: String) -> i32 {
        let mut res = 0;
        let mut left = 0;
        for c in s.chars() {
            if c == '(' {
                left += 1;
                res = max(res, left);
            }
            if c == ')' {
                left -= 1;
            }
        }
        res
    }
}

#[test]
fn test_max_depth() {
    assert_eq!(3, Solution::max_depth("(1+(2*3)+((8)/4))+1".to_string()));
    assert_eq!(3, Solution::max_depth("(1)+((2))+(((3)))".to_string()));
    assert_eq!(1, Solution::max_depth("1+(2*3)/(2-1)".to_string()));
    assert_eq!(0, Solution::max_depth("0".to_string()));
}
