struct Solution;

impl Solution {
    pub fn ways_to_make_fair(nums: Vec<i32>) -> i32 {
        let mut left = vec![0; 2];
        let mut right = vec![0; 2];
        let mut res = 0;
        for (i, v) in nums.iter().enumerate() {
            right[i % 2] += v;
        }
        for (i, v) in nums.iter().enumerate() {
            right[i % 2] -= v;
            if left[0] + right[1] == left[1] + right[0] {
                res += 1;
            }
            left[i % 2] += v;
        }
        res
    }
}

#[test]
fn test_ways_to_make_fair() {
    assert_eq!(1, Solution::ways_to_make_fair(vec![2, 1, 6, 4]));
    assert_eq!(3, Solution::ways_to_make_fair(vec![1, 1, 1]));
    assert_eq!(0, Solution::ways_to_make_fair(vec![1, 2, 3]));
}
