struct Solution;

impl Solution {
    pub fn check(nums: Vec<i32>) -> bool {
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
