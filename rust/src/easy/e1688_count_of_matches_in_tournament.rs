struct Solution;

impl Solution {
    pub fn number_of_matches(n: i32) -> i32 {
        n - 1
    }
}

#[test]
fn test_number_of_matches() {
    assert_eq!(6, Solution::number_of_matches(7));
    assert_eq!(13, Solution::number_of_matches(14));
}
