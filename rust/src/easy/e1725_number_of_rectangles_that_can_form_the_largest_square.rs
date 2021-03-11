use std::cmp::{max, min};
use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn count_good_rectangles(rectangles: Vec<Vec<i32>>) -> i32 {
        let mut map = HashMap::<i32, i32>::new();
        for rectangle in rectangles {
            let max_len = min(rectangle[0], rectangle[1]);
            *map.entry(max_len).or_insert(0) += 1;
        }
        let mut max_key = 0;
        let mut res = 0;
        for (key, value) in map.into_iter() {
            if key > max_key {
                res = value;
                max_key = key;
            }
        }
        res
    }
}

#[test]
fn test_count_good_rectangles() {
    assert_eq!(
        3,
        Solution::count_good_rectangles(vec![vec![5, 8], vec![3, 9], vec![5, 12], vec![16, 5]])
    );
    assert_eq!(
        3,
        Solution::count_good_rectangles(vec![vec![2, 3], vec![3, 7], vec![4, 3], vec![3, 7]])
    );
    assert_eq!(
        1,
        Solution::count_good_rectangles(vec![vec![5, 8], vec![3, 9], vec![3, 12]])
    );
}
