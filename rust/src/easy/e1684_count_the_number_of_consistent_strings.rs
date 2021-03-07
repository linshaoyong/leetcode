use std::collections::HashSet;
use std::convert::TryInto;

struct Solution;

impl Solution {
    pub fn count_consistent_strings(allowed: String, words: Vec<String>) -> i32 {
        let hs = allowed.chars().collect::<HashSet<char>>();
        let mut res = words.len();
        for word in words {
            for c in word.chars() {
                if !hs.contains(&c) {
                    res -= 1;
                    break;
                }
            }
        }
        res.try_into().unwrap()
    }
}

#[test]
fn test_count_consistent_strings_1() {
    assert_eq!(
        2,
        Solution::count_consistent_strings(
            "ab".to_string(),
            vec![
                "ad".to_string(),
                "bd".to_string(),
                "aaab".to_string(),
                "baa".to_string(),
                "badab".to_string()
            ]
        )
    )
}

#[test]
fn test_count_consistent_strings_2() {
    assert_eq!(
        7,
        Solution::count_consistent_strings(
            "abc".to_string(),
            vec![
                "a".to_string(),
                "b".to_string(),
                "c".to_string(),
                "ab".to_string(),
                "ac".to_string(),
                "bc".to_string(),
                "abc".to_string()
            ]
        )
    )
}

#[test]
fn test_count_consistent_strings_3() {
    assert_eq!(
        4,
        Solution::count_consistent_strings(
            "cad".to_string(),
            vec![
                "cc".to_string(),
                "acd".to_string(),
                "b".to_string(),
                "ba".to_string(),
                "bac".to_string(),
                "bad".to_string(),
                "ac".to_string(),
                "d".to_string()
            ]
        )
    )
}
