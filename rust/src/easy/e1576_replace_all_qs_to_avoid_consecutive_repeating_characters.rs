use std::collections::HashSet;

struct Solution;

impl Solution {
    pub fn modify_string(s: String) -> String {
        let mut cs: Vec<char> = s.chars().collect();
        let mut excludes: HashSet<char> = HashSet::new();
        let abc = vec!['a', 'b', 'c'];
        for i in 0..cs.len() {
            if cs[i] == '?' {
                if i > 0 {
                    excludes.insert(cs[i - 1]);
                }
                if i < cs.len() - 1 {
                    excludes.insert(cs[i + 1]);
                }
                for cc in &abc {
                    if !excludes.contains(&cc) {
                        cs[i] = *cc;
                        break;
                    }
                }
                excludes.clear();
            }
        }
        cs.iter().collect()
    }
}

#[test]
fn test_modify_string() {
    assert_eq!("azs", Solution::modify_string("?zs".to_string()));
    assert_eq!("ubvaw", Solution::modify_string("ubv?w".to_string()));
    assert_eq!("jaqgacb", Solution::modify_string("j?qg??b".to_string()));
    assert_eq!(
        "abywaipkja",
        Solution::modify_string("??yw?ipkj?".to_string())
    );
}
