struct Solution;

impl Solution {
    pub fn smallest_divisor(nums: Vec<i32>, threshold: i32) -> i32 {
        let nums_cloned = &nums.clone();
        let mut left = 1;
        let mut right = *nums.iter().max().unwrap();
        while left < right {
            let mid = left + (right - left) / 2;
            if feasible(mid, threshold, nums_cloned) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        left
    }
}

fn feasible(divisor: i32, threshold: i32, nums: &Vec<i32>) -> bool {
    let mut res = 0;
    for n in nums {
        res += (n - 1) / divisor + 1;
        if res > threshold {
            return false;
        }
    }
    true
}

#[test]
fn test_smallest_divisor() {
    assert_eq!(5, Solution::smallest_divisor(vec![1, 2, 5, 9], 6));
    assert_eq!(44, Solution::smallest_divisor(vec![44, 22, 33, 11, 1], 5));
    assert_eq!(
        1,
        Solution::smallest_divisor(vec![21212, 10101, 12121], 1000000)
    );
    assert_eq!(3, Solution::smallest_divisor(vec![2, 3, 5, 7, 11], 11));
}
