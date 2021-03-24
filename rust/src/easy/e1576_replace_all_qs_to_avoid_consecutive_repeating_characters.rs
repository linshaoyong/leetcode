struct Solution;

impl Solution {
    pub fn modify_string(s: String) -> String {
        "".to_string()
    }
}

#[test]
fn test_modify_string() {
    assert_eq!("azs", Solution::modify_string("?zs".to_string()));
    assert_eq!("ubvaw", Solution::modify_string("ubv?w".to_string()));
    assert_eq!("jaqgacb", Solution::modify_string("j?qg??b".to_string()));
    assert_eq!(
        "acywaipkja",
        Solution::modify_string("??yw?ipkj?".to_string())
    );
}
