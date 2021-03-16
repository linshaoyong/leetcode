use core::cmp::max;
use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn max_length_between_equal_characters(s: String) -> i32 {
        let mut map = HashMap::<char, Vec<i32>>::new();
        for (i, c) in s.chars().enumerate() {
            match map.get_mut(&c) {
                Some(vvv) => {
                    vvv[1] = i as i32 - vvv[0] - 1;
                }
                None => {
                    map.insert(c, vec![i as i32, -1]);
                }
            }
        }
        let mut res = -1;
        for (_, value) in map.iter() {
            res = max(res, value[1]);
        }
        res
    }
}

#[test]
fn test_max_length_between_equal_characters() {
    assert_eq!(
        0,
        Solution::max_length_between_equal_characters("aa".to_string())
    );
    assert_eq!(
        2,
        Solution::max_length_between_equal_characters("abca".to_string())
    );
    assert_eq!(
        -1,
        Solution::max_length_between_equal_characters("cbzxy".to_string())
    );
    assert_eq!(
        4,
        Solution::max_length_between_equal_characters("cabbac".to_string())
    );
}
