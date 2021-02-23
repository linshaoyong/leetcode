struct Solution;

impl Solution {
    pub fn maximum_wealth(accounts: Vec<Vec<i32>>) -> i32 {
        let mut res = 0;
        for account in accounts {
            res = std::cmp::max(res, account.iter().sum());
        }
        res
    }
}

#[test]
pub fn test_maximum_wealth() {
    let v = vec![vec![1, 2, 3], vec![3, 2, 1]];
    assert_eq!(6, Solution::maximum_wealth(v));

    let v = vec![vec![1, 5], vec![7, 3], vec![3, 5]];
    assert_eq!(10, Solution::maximum_wealth(v));

    let v = vec![vec![2, 8, 7], vec![7, 1, 3], vec![1, 9, 5]];
    assert_eq!(17, Solution::maximum_wealth(v));
}
