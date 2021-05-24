use std::cmp;

struct Solution;

impl Solution {
    pub fn check_zero_ones(s: String) -> bool {
        let mut max_zeros = 0;
        let mut max_ones = 0;
        let mut contiguous = 0;
        let chars = &mut s.chars().collect::<Vec<char>>();
        let mut prev = chars[0];
        for i in 0..chars.len() {
            let current = chars[i];
            if current == prev {
                contiguous += 1;
                if i == chars.len() - 1 {
                    if current == '1' {
                        max_ones = cmp::max(max_ones, contiguous);
                    } else {
                        max_zeros = cmp::max(max_zeros, contiguous);
                    }
                }
            } else {
                if current == '1' {
                    max_zeros = cmp::max(max_zeros, contiguous);
                } else {
                    max_ones = cmp::max(max_ones, contiguous);
                }
                contiguous = 1;
            }
            prev = current;
        }
        max_ones > max_zeros
    }
}

#[test]
fn test_check_zero_ones() {
    assert_eq!(true, Solution::check_zero_ones("1101".to_string()));
    assert_eq!(false, Solution::check_zero_ones("111000".to_string()));
    assert_eq!(false, Solution::check_zero_ones("110100010".to_string()));
}
