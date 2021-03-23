use std::cmp::min;

struct Solution;

impl Solution {
    pub fn min_operations(s: String) -> i32 {
        let mut op1 = 0;
        let mut op2 = 0;
        for (i, c) in s.chars().enumerate() {
            if i % 2 == 0 {
                if c == '1' {
                    op1 += 1;
                } else {
                    op2 += 1;
                }
            } else {
                if c == '0' {
                    op1 += 1;
                } else {
                    op2 += 1;
                }
            }
        }
        min(op1, op2)
    }
}

#[test]
fn test_min_operations() {
    assert_eq!(1, Solution::min_operations("0100".to_string()));
    assert_eq!(0, Solution::min_operations("10".to_string()));
    assert_eq!(2, Solution::min_operations("1111".to_string()));
}
