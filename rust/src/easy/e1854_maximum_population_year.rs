struct Solution;

impl Solution {
    pub fn maximum_population(logs: Vec<Vec<i32>>) -> i32 {
        0
    }
}

#[test]
fn test_maximum_population() {
    assert_eq!(
        1993,
        Solution::maximum_population(vec![vec![1993, 1999], vec![2000, 2010]])
    );
    assert_eq!(
        1960,
        Solution::maximum_population(vec![vec![1950, 1961], vec![1960, 1971], vec![1970, 1981]])
    );
}
