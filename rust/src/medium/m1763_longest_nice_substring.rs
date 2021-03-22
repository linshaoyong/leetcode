use std::collections::HashSet;
use std::iter::FromIterator;

struct Solution;

impl Solution {
    pub fn longest_nice_substring(s: String) -> String {
        let sbs = s.as_bytes();
        let mut bytes: HashSet<u8> = HashSet::from_iter(sbs.iter().cloned());
        if sbs.len() < 2 {
            return "".to_string();
        }

        for (i, b) in sbs.iter().enumerate() {
            let opp = if *b < 97 { *b + 32 } else { *b - 32 };
            if !bytes.contains(&opp) {
                let s0 = Solution::longest_nice_substring(
                    String::from_utf8_lossy(&sbs[0..i]).to_string(),
                );
                let s1 = Solution::longest_nice_substring(
                    String::from_utf8_lossy(&sbs[i + 1..]).to_string(),
                );
                if s0.len() >= s1.len() {
                    return s0;
                } else {
                    return s1;
                }
            }
        }
        s
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
