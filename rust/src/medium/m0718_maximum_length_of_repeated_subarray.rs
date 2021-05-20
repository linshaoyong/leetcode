use std::cmp;

struct Solution;

impl Solution {
    pub fn find_length(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let cloned1 = &nums1.clone();
        let cloned2 = &nums2.clone();
        let mut left = 0;
        let mut right = cmp::min(nums1.len() as i32, nums2.len() as i32);
        while left < right {
            let mid = left + (right + 1 - left) / 2;
            if feasible(mid as usize, cloned1, cloned2) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        left
    }
}

fn feasible(m: usize, nums1: &Vec<i32>, nums2: &Vec<i32>) -> bool {
    for i in 0..nums1.len() + 1 - m {
        for j in 0..nums2.len() + 1 - m {
            if nums1[i..i + m] == nums2[j..j + m] {
                return true;
            }
        }
    }
    false
}

#[test]
fn test_find_length() {
    assert_eq!(
        3,
        Solution::find_length(vec![1, 2, 3, 2, 1], vec![3, 2, 1, 4, 7])
    );
    assert_eq!(
        5,
        Solution::find_length(vec![0, 0, 0, 0, 0], vec![0, 0, 0, 0, 0])
    );
}
