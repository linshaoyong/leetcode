struct Solution;

impl Solution {
    pub fn sum_odd_length_subarrays(arr: Vec<i32>) -> i32 {
        let mut res = 0;
        for i in 0..arr.len() {
            let start = arr.len() - i;
            let end = i + 1;
            let total = start * end;
            let mut odd = total / 2;
            if total % 2 == 1 {
                odd += 1;
            }
            res += (odd as i32) * arr[i];
        }
        res
    }
}

#[test]
fn test_sum_odd_length_subarrays() {
    assert_eq!(58, Solution::sum_odd_length_subarrays(vec![1, 4, 2, 5, 3]));
    assert_eq!(3, Solution::sum_odd_length_subarrays(vec![1, 2]));
    assert_eq!(66, Solution::sum_odd_length_subarrays(vec![10, 11, 12]));
}
