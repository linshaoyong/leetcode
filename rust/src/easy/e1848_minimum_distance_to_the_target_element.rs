use std::cmp::min;

struct Solution;

impl Solution {
    pub fn get_min_distance(nums: Vec<i32>, target: i32, start: i32) -> i32 {
        let mut res = nums.len() as i32;
        for (i, v) in nums.iter().enumerate() {
            if *v == target {
                res = min(res, (i as i32 - start).abs());
            }
        }
        res
    }
}

#[test]
fn test_get_min_distance() {
    assert_eq!(1, Solution::get_min_distance(vec![1, 2, 3, 4, 5], 5, 3));
    assert_eq!(0, Solution::get_min_distance(vec![1], 1, 0));
    assert_eq!(
        0,
        Solution::get_min_distance(vec![1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1, 0)
    );
}
