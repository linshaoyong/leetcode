struct Solution;

impl Solution {
    pub fn sort_sentence(s: String) -> String {
        "".to_string()
    }
}

#[test]
fn test_sort_sentence() {
    assert_eq!(
        "This is a sentence",
        Solution::sort_sentence("is2 sentence4 This1 a3".to_string())
    );
    assert_eq!(
        "Me Myself and I",
        Solution::sort_sentence("Myself2 Me1 I4 and3".to_string())
    );
}
