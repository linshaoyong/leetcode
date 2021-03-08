struct Solution;

impl Solution {
    pub fn merge_alternately(word1: String, word2: String) -> String {
        let c1: Vec<char> = word1.chars().collect();
        let c2: Vec<char> = word2.chars().collect();
        let longer = std::cmp::max(c1.len(), c2.len());
        let mut res = String::from("");
        for i in 0..longer {
            if i < c1.len() {
                res.push(*c1.get(i).unwrap());
            }
            if i < c2.len() {
                res.push(*c2.get(i).unwrap());
            }
        }
        res
    }
}

#[test]
fn test_merge_alternately() {
    assert_eq!(
        "apbqcr".to_string(),
        Solution::merge_alternately("abc".to_string(), "pqr".to_string())
    );

    assert_eq!(
        "apbqrs".to_string(),
        Solution::merge_alternately("ab".to_string(), "pqrs".to_string())
    );

    assert_eq!(
        "apbqcd".to_string(),
        Solution::merge_alternately("abcd".to_string(), "pq".to_string())
    );
}
