struct Solution;

impl Solution {
    pub fn split_array(nums: Vec<i32>, m: i32) -> i32 {
        let nums_cloned = &nums.clone();
        let mut left: i32 = *nums.iter().max().unwrap();
        let mut right: i32 = nums.iter().sum();
        while left < right {
            let mid = left + (right - left) / 2;
            if feasible(mid, m, nums_cloned) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        left
    }
}

fn feasible(threshold: i32, m: i32, nums: &Vec<i32>) -> bool {
    let mut count = 1;
    let mut total = 0;
    for num in nums {
        total += num;
        if total > threshold {
            total = *num;
            count += 1;
            if count > m {
                return false;
            }
        }
    }
    true
}

#[test]
fn test_split_array() {
    assert_eq!(18, Solution::split_array(vec![7, 2, 5, 10, 8], 2));
    assert_eq!(9, Solution::split_array(vec![1, 2, 3, 4, 5], 2));
    assert_eq!(4, Solution::split_array(vec![1, 4, 4], 3));
}
