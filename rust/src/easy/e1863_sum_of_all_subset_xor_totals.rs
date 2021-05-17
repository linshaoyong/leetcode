struct Solution;

impl Solution {
    pub fn subset_xor_sum(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut res = 0;
        for v in nums {
            res |= v;
        }
        res * 2_i32.pow(n as u32 - 1)
    }
}

#[test]
fn test_subset_xor_sum() {
    assert_eq!(6, Solution::subset_xor_sum(vec![1, 3]));
    assert_eq!(28, Solution::subset_xor_sum(vec![5, 1, 6]));
    assert_eq!(480, Solution::subset_xor_sum(vec![3, 4, 5, 6, 7, 8]));
}
