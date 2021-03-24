struct Solution;

impl Solution {
    pub fn max_repeating(sequence: String, word: String) -> i32 {
        0
    }
}

#[test]
fn test_max_repeating() {
    assert_eq!(
        2,
        Solution::max_repeating("ababc".to_string(), "ab".to_string())
    );
    assert_eq!(
        1,
        Solution::max_repeating("ababc".to_string(), "ba".to_string())
    );
    assert_eq!(
        0,
        Solution::max_repeating("ababc".to_string(), "ac".to_string())
    );
}
