struct Solution;

impl Solution {
    pub fn contains_pattern(arr: Vec<i32>, m: i32, k: i32) -> bool {
        let mut count = 1;
        let m = m as usize;
        for i in 0..m {
            for j in (i + m..arr.len()).step_by(m) {
                if j + m > arr.len() {
                    break;
                }
                if &arr[j - m..j] == &arr[j..j + m] {
                    count += 1;
                    if count >= k {
                        return true;
                    }
                } else {
                    count = 1;
                }
            }
        }
        false
    }
}

#[test]
fn test_contains_pattern() {
    assert_eq!(
        true,
        Solution::contains_pattern(vec![1, 2, 4, 4, 4, 4], 1, 3)
    );
    assert_eq!(
        true,
        Solution::contains_pattern(vec![1, 2, 1, 2, 1, 1, 1, 3], 2, 2)
    );
    assert_eq!(
        false,
        Solution::contains_pattern(vec![1, 2, 1, 2, 1, 3], 2, 3)
    );
    assert_eq!(false, Solution::contains_pattern(vec![1, 2, 3, 1, 2], 2, 2));
    assert_eq!(false, Solution::contains_pattern(vec![2, 2, 2, 2], 2, 3));
    assert_eq!(true, Solution::contains_pattern(vec![2, 2], 1, 2));
    assert_eq!(
        true,
        Solution::contains_pattern(vec![3, 2, 2, 1, 2, 2, 1, 1, 1, 2, 3, 2, 2], 3, 2)
    );
    assert_eq!(
        false,
        Solution::contains_pattern(vec![2, 1, 2, 1, 1, 2, 1, 2, 2, 1, 2, 2, 2], 1, 4)
    );
}
