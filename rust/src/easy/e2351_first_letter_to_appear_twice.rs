use std::collections::HashSet;
use std::iter::FromIterator;

struct Solution;

impl Solution {
    pub fn repeated_character(s: String) -> char {
        let mut cs = HashSet::new();
        for c in s.chars() {
            if cs.contains(&c) {
                return c;
            }
            cs.insert(c);
        }
        'a'
    }
}

#[test]
fn test_count_good_substrings() {
    assert_eq!('x', Solution::repeated_character("xxxx".to_string()));
    assert_eq!('c', Solution::repeated_character("abccbaacz".to_string()));
    assert_eq!('d', Solution::repeated_character("abcdd".to_string()));
}
