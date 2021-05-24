use std::cmp::Reverse;
use std::collections::BinaryHeap;

struct Solution;

impl Solution {
    pub fn furthest_building(heights: Vec<i32>, mut bricks: i32, ladders: i32) -> i32 {
        let mut heap = BinaryHeap::new();
        let mut mut_bricks = bricks;
        for i in 0..heights.len() - 1 {
            let mut d = heights[i + 1] - heights[i];
            if d > 0 {
                heap.push(Reverse(d));
            }
            if heap.len() as i32 > ladders {
                if let Some(Reverse(v)) = heap.pop() {
                    mut_bricks -= v;
                }
            }
            if mut_bricks < 0 {
                return i as i32;
            }
        }
        heights.len() as i32 - 1
    }
}

#[test]
fn test_furthest_building() {
    assert_eq!(1, Solution::furthest_building(vec![7, 5, 13], 0, 0));
    assert_eq!(
        4,
        Solution::furthest_building(vec![4, 2, 7, 6, 9, 14, 12], 5, 1)
    );
    assert_eq!(
        7,
        Solution::furthest_building(vec![4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2)
    );
    assert_eq!(3, Solution::furthest_building(vec![14, 3, 19, 3], 17, 0));
}
