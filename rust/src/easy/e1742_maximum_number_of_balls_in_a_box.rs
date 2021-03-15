use core::cmp::max;
use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn count_balls(low_limit: i32, high_limit: i32) -> i32 {
        let mut map = HashMap::<i32, i32>::new();
        for mut ball in low_limit..high_limit + 1 {
            let mut key = 0;
            while ball > 0 {
                key += ball % 10;
                ball = ball / 10;
            }
            *map.entry(key).or_insert(0) += 1;
        }

        let mut res = 0;
        for (_, v) in map.iter() {
            res = max(*v, res);
        }
        res
    }
}

#[test]
fn test_count_balls() {
    assert_eq!(2, Solution::count_balls(1, 10));
    assert_eq!(2, Solution::count_balls(5, 15));
    assert_eq!(2, Solution::count_balls(19, 28));
    assert_eq!(9, Solution::count_balls(11, 104));
}
