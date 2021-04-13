struct Solution;

impl Solution {
    pub fn min_operations(n: i32) -> i32 {
        let mut res = 0;
        for i in 0..n / 2 {
            res += n - 2 * i - 1;
        }
        res
    }
}

#[test]
fn test_min_operations() {
    assert_eq!(2, Solution::min_operations(3));
    assert_eq!(9, Solution::min_operations(6));
}
