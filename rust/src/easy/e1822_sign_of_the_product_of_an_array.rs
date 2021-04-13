struct Solution;

impl Solution {
    pub fn array_sign(nums: Vec<i32>) -> i32 {
        let mut odds = 0;
        for n in nums {
            if n == 0 {
                return 0;
            }
            if n < 0 {
                odds += 1;
            }
        }
        match odds % 2 {
            0 => 1,
            _ => -1,
        }
    }
}

#[test]
fn test_array_sign() {
    assert_eq!(1, Solution::array_sign(vec![-1, -2, -3, -4, 3, 2, 1]));
    assert_eq!(0, Solution::array_sign(vec![1, 5, 0, 2, -3]));
    assert_eq!(-1, Solution::array_sign(vec![-1, 1, -1, 1, -1]));
}
