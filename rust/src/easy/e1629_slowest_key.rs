use std::collections::HashSet;

struct Solution;

impl Solution {
    pub fn slowest_key(release_times: Vec<i32>, keys_pressed: String) -> char {
        let mut max_duration = 0;
        let chars: Vec<char> = keys_pressed.chars().collect();
        let mut max_chars = vec![];
        for (i, time) in release_times.iter().enumerate() {
            if i == 0 {
                max_duration = *time;
                max_chars.push(chars[i]);
            } else {
                let duration = time - release_times[i - 1];
                if duration >= max_duration {
                    if duration > max_duration {
                        max_duration = duration;
                        max_chars.clear();
                    }
                    max_chars.push(chars[i]);
                }
            }
        }
        *max_chars.iter().max().unwrap()
    }
}

#[test]
fn test_slowest_key() {
    assert_eq!(
        'c',
        Solution::slowest_key(vec![9, 29, 49, 50], "cbcd".to_string())
    );

    assert_eq!(
        'a',
        Solution::slowest_key(vec![12, 23, 36, 46, 62], "spuda".to_string())
    );
}
