use std::collections::HashSet;

struct Solution;

impl Solution {
    pub fn check_if_pangram(sentence: String) -> bool {
        let alphet: HashSet<char> = sentence.chars().into_iter().collect();
        alphet.len() == 26
    }
}

#[test]
fn test_check_if_pangram() {
    assert_eq!(
        true,
        Solution::check_if_pangram("thequickbrownfoxjumpsoverthelazydog".to_string())
    );
    assert_eq!(false, Solution::check_if_pangram("leetcode".to_string()));
}
