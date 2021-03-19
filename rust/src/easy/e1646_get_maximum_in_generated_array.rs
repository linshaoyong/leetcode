use std::cmp::max;

struct Solution;

impl Solution {
    pub fn get_maximum_generated(n: i32) -> i32 {
        if n == 0 {
            return 0;
        }
        let mut nums = vec![0; (n + 1) as usize];
        nums[1] = 1;
        let mut maximum = 1;
        let i = (n + 1) / 2;
        for j in 1..i {
            let k = j as usize;
            nums[2 * k] = nums[k];
            nums[2 * k + 1] = nums[k] + nums[k + 1];
            maximum = max(maximum, nums[2 * k]);
            maximum = max(maximum, nums[2 * k + 1]);
        }
        maximum
    }
}

#[test]
fn test_get_maximum_generated() {
    assert_eq!(3, Solution::get_maximum_generated(7));
    assert_eq!(1, Solution::get_maximum_generated(2));
    assert_eq!(2, Solution::get_maximum_generated(3));
    assert_eq!(1, Solution::get_maximum_generated(1));
}
