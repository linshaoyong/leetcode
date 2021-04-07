struct Solution;

impl Solution {
    pub fn truncate_sentence(s: String, k: i32) -> String {
        let vs: Vec<&str> = s.split(' ').collect();
        vs[..k as usize].join(" ")
    }
}

#[test]
fn test_truncate_sentence() {
    assert_eq!(
        "Hello how are you",
        Solution::truncate_sentence("Hello how are you Contestant".to_string(), 4)
    );

    assert_eq!(
        "What is the solution",
        Solution::truncate_sentence("What is the solution to this problem".to_string(), 4)
    );

    assert_eq!(
        "chopper is not a tanuki",
        Solution::truncate_sentence("chopper is not a tanuki".to_string(), 5)
    );
}
