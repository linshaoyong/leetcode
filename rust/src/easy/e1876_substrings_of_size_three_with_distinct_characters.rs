use std::collections::HashSet;
use std::iter::FromIterator;

struct Solution;

impl Solution {
    pub fn count_good_substrings(s: String) -> i32 {
        let mut res = 0;
        let chars = &mut s.chars().collect::<Vec<char>>();
        if chars.len() < 3 {
            return res;
        }
        for i in 0..chars.len() - 2 {
            let sub = &chars[i..i + 3];
            let sub_set: HashSet<char> = sub.iter().cloned().collect();
            if sub_set.len() == 3 {
                res += 1;
            }
        }
        res
    }
}

#[test]
fn test_count_good_substrings() {
    assert_eq!(0, Solution::count_good_substrings("x".to_string()));
    assert_eq!(1, Solution::count_good_substrings("xyzzaz".to_string()));
    assert_eq!(4, Solution::count_good_substrings("aababcabc".to_string()));
}
