struct Solution;

impl Solution {
    pub fn check_ones_segment(s: String) -> bool {
        if s.len() == 1 {
            return true;
        }
        let mut zeros = 0;
        for c in s.chars() {
            if c == '1' {
                if zeros > 0 {
                    return false;
                }
            } else {
                zeros = 1;
            }
        }
        true
    }
}

#[test]
fn test_check_ones_segment() {
    assert!(Solution::check_ones_segment("1001".to_string()) == false);
    assert!(Solution::check_ones_segment("110".to_string()));
    assert!(Solution::check_ones_segment("1".to_string()));
    assert!(Solution::check_ones_segment("10".to_string()));
}
