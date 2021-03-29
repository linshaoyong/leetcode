use std::collections::HashSet;

struct Solution;

impl Solution {
    pub fn num_different_integers(word: String) -> i32 {
        let mut integers = HashSet::<String>::new();
        let mut integer = String::from("");
        for c in word.chars() {
            if c.is_digit(10) {
                if c == '0' {
                    if integer.len() == 0 || integer[0..1] != *"0" {
                        integer.push(c);
                    }
                } else {
                    if integer.len() == 1 && integer[0..1] == *"0" {
                        integer.clear();
                    }
                    integer.push(c);
                }
            } else {
                if integer.len() > 0 {
                    integers.insert(integer.clone());
                    integer.clear();
                }
            }
        }
        if integer.len() > 0 {
            integers.insert(integer.clone());
        }
        integers.len() as i32
    }
}

#[test]
fn test_num_different_integers() {
    assert_eq!(
        3,
        Solution::num_different_integers("a123bc34d8ef34".to_string())
    );
    assert_eq!(
        2,
        Solution::num_different_integers("leet1234code234".to_string())
    );
    assert_eq!(1, Solution::num_different_integers("a1b01c001".to_string()));

    assert_eq!(
        1,
        Solution::num_different_integers("167278959591294".to_string())
    );
}
