struct Solution;

impl Solution {
    pub fn sort_sentence(s: String) -> String {
        let splits: Vec<&str> = s.split(' ').collect();
        let mut sentences = vec![""; splits.len()];
        for split in splits {
            let bs = split.as_bytes();
            let i = (bs[bs.len() - 1] - 49) as usize;
            sentences[i] = std::str::from_utf8(&bs[0..bs.len() - 1]).unwrap();
        }
        sentences.join(" ")
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
