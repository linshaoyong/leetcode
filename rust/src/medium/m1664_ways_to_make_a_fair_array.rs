struct Solution;

impl Solution {
    pub fn ways_to_make_fair(nums: Vec<i32>) -> i32 {
        0
    }
}

#[test]
fn test_ways_to_make_fair() {
    assert_eq!(1, Solution::ways_to_make_fair(vec![2, 1, 6, 4]));
    assert_eq!(3, Solution::ways_to_make_fair(vec![1, 1, 1]));
    assert_eq!(0, Solution::ways_to_make_fair(vec![1, 2, 3]));
}
