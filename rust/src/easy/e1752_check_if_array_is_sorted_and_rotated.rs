struct Solution;

impl Solution {
    pub fn check(nums: Vec<i32>) -> bool {
        let mut down = 0;
        for i in 1..nums.len() {
            if nums[i] < nums[i - 1] {
                down += 1;
                if down > 1 {
                    return false;
                }
            }
        }
        if down == 1 && nums[nums.len() - 1] > nums[0] {
            return false;
        }
        true
    }
}

#[test]
fn test_check() {
    assert!(Solution::check(vec![3, 4, 5, 1, 2]));
    assert!(Solution::check(vec![2, 1, 3, 4]) == false);
    assert!(Solution::check(vec![1, 2, 3]));
    assert!(Solution::check(vec![1, 1, 1]));
    assert!(Solution::check(vec![2, 1]));
}
