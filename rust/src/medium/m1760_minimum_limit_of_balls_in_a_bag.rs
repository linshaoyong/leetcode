struct Solution;

impl Solution {
    pub fn minimum_size(nums: Vec<i32>, max_operations: i32) -> i32 {
        let mut left = 1;
        let mut right = *nums.iter().max().unwrap();
        while left < right {
            let mid = left + (right - left) / 2;
            let mut operations = 0;
            for num in &nums {
                operations += (num - 1) / mid;
            }
            if operations > max_operations {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        left
    }
}

#[test]
fn test_minimum_size() {
    assert_eq!(3, Solution::minimum_size(vec![9], 2));
    assert_eq!(2, Solution::minimum_size(vec![2, 4, 8, 2], 4));
    assert_eq!(7, Solution::minimum_size(vec![7, 17], 2));
}
