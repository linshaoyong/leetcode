use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn four_sum_count(
        nums1: Vec<i32>,
        nums2: Vec<i32>,
        nums3: Vec<i32>,
        nums4: Vec<i32>,
    ) -> i32 {
        let mut ab = HashMap::<i32, i32>::new();
        for i in nums1 {
            for j in &nums2 {
                *ab.entry(i + j).or_insert(0) += 1;
            }
        }
        let mut ans = 0;
        for i in nums3 {
            for j in &nums4 {
                ans += ab.get(&(-i - j)).cloned().unwrap_or(0);
            }
        }
        ans
    }
}

#[test]
fn test_four_sum_count() {
    assert_eq!(
        2,
        Solution::four_sum_count(vec![1, 2], vec![-2, -1], vec![-1, 2], vec![0, 2])
    );
    assert_eq!(
        1,
        Solution::four_sum_count(vec![0], vec![0], vec![0], vec![0])
    );
}
