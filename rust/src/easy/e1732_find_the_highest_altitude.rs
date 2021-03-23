struct Solution;

impl Solution {
    pub fn largest_altitude(gain: Vec<i32>) -> i32 {
        let mut res = 0;
        let mut cur = 0;
        for v in gain {
            cur += v;
            res = core::cmp::max(res, cur);
        }
        res
    }
}

#[test]
fn test_largest_altitude() {
    assert_eq!(1, Solution::largest_altitude(vec![-5, 1, 5, 0, -7]));
    assert_eq!(0, Solution::largest_altitude(vec![-4, -3, -2, -1, 4, 3, 2]));
}
