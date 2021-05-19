struct Solution;

impl Solution {
    pub fn nth_ugly_number(n: i32, a: i32, b: i32, c: i32) -> i32 {
        let mut left = 1;
        let mut right = 1000000000;
        while left < right {
            let mid = left + (right - left) / 2;
            if feasible(mid) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        left
    }
}

fn feasible(num: i32) -> bool {
    true
}

#[test]
fn test_nth_ugly_number() {
    assert_eq!(4, Solution::nth_ugly_number(3, 2, 3, 5));
    assert_eq!(6, Solution::nth_ugly_number(4, 2, 3, 4));
    assert_eq!(10, Solution::nth_ugly_number(5, 2, 11, 13));
    assert_eq!(
        1999999984,
        Solution::nth_ugly_number(1000000000, 2, 217983653, 336916467)
    );
}
