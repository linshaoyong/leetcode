struct Solution;

impl Solution {
    pub fn longest_nice_substring(s: String) -> String {
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
