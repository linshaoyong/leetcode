struct Solution;

impl Solution {
    pub fn sum_base(n: i32, k: i32) -> i32 {
        let mut res = 0;
        let mut bn = n;
        while bn > 0 {
            res += bn % k;
            bn = bn / k;
        }
        res
    }
}

#[test]
fn test_sum_base() {
    assert_eq!(9, Solution::sum_base(34, 6));
    assert_eq!(1, Solution::sum_base(10, 10));
}
