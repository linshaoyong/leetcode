use core::cmp::max;

struct Solution;

impl Solution {
    pub fn max_ascending_sum(nums: Vec<i32>) -> i32 {
        let mut max_sum = nums[0];
        let mut cur_max_sum = nums[0];
        for i in 1..nums.len() {
            if nums[i] > nums[i - 1] {
                cur_max_sum += nums[i];
            } else {
                max_sum = max(max_sum, cur_max_sum);
                cur_max_sum = nums[i];
            }
        }
        max(max_sum, cur_max_sum)
    }
}

#[test]
fn test_max_ascending_sum() {
    assert_eq!(65, Solution::max_ascending_sum(vec![10, 20, 30, 5, 10, 50]));
    assert_eq!(150, Solution::max_ascending_sum(vec![10, 20, 30, 40, 50]));
    assert_eq!(
        33,
        Solution::max_ascending_sum(vec![12, 17, 15, 13, 10, 11, 12])
    );
    assert_eq!(100, Solution::max_ascending_sum(vec![100, 10, 1]));
}
