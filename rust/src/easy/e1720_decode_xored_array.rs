struct Solution;

impl Solution {
    pub fn decode(encoded: Vec<i32>, first: i32) -> Vec<i32> {
        let mut res = vec![first; encoded.len() + 1];
        for (i, v) in encoded.iter().enumerate() {
            res[i + 1] = res[i] ^ v;
        }
        res
    }
}

#[test]
fn test_decode() {
    assert_eq!(vec![1, 0, 2, 1], Solution::decode(vec![1, 2, 3], 1));
    assert_eq!(vec![4, 2, 0, 7, 4], Solution::decode(vec![6, 2, 7, 3], 4));
}
