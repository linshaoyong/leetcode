struct Solution;

impl Solution {
    pub fn k_length_apart(nums: Vec<i32>, k: i32) -> bool {
        let mut start = 0;
        let mut index = 0;
        for num in nums {
            index += 1;
            if num == 1 {
                if start < 1 {
                    start = index;
                    continue;
                }
                if index - start - 1 < k {
                    return false;
                }
                start = index;
            }
        }
        true
    }
}

#[test]
fn test_k_length_apart() {
    assert!(Solution::k_length_apart(vec![1, 0, 0, 0, 1, 0, 0, 1], 2));
    assert!(!Solution::k_length_apart(vec![1, 0, 0, 1, 0, 1], 2));
    assert!(Solution::k_length_apart(vec![1, 1, 1, 1, 1], 0));
    assert!(Solution::k_length_apart(vec![0, 1, 0, 1], 1));
}
