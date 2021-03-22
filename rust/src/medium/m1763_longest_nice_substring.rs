use std::collections::HashSet;
use std::iter::FromIterator;

struct Solution;

impl Solution {
    pub fn longest_nice_substring(s: String) -> String {
        let sbs = s.as_bytes();
        let mut bytes: HashSet<u8> = HashSet::from_iter(sbs.iter().cloned());
        for i in 0..sbs.len() {
            bytes.insert(sbs[i]);
        }

        let mut not_nice_indexs: Vec<i32> = vec![];
        for i in 0..sbs.len() {
            if sbs[i] < 97 {}
            let nice_char = if sbs[i] < 97 {
                sbs[i] + 32
            } else {
                sbs[i] - 32
            };
            if !bytes.contains(&nice_char) {
                not_nice_indexs.push(i as i32);
            }
        }
        "".to_string()
    }
}

#[test]
fn test_longest_nice_substring() {
    assert_eq!(
        "aAa",
        Solution::longest_nice_substring("YazaAay".to_string())
    );
    assert_eq!("Bb", Solution::longest_nice_substring("Bb".to_string()));
    assert_eq!("", Solution::longest_nice_substring("c".to_string()));
    assert_eq!("dD", Solution::longest_nice_substring("dDzeE".to_string()));
}
