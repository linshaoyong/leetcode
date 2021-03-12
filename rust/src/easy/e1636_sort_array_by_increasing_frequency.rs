use std::cmp::Ordering;
use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn frequency_sort(nums: Vec<i32>) -> Vec<i32> {
        let mut hm: HashMap<i32, i64> = nums.iter().fold(HashMap::new(), |mut hm, n| {
            *hm.entry(*n).or_insert(0) += 1;
            hm
        });

        let mut frequencs: Vec<(&i32, &i64)> = hm.iter().collect();
        frequencs.sort_by(|a, b| match a.1.cmp(&b.1) {
            Ordering::Equal => b.0.cmp(&a.0),
            other => other,
        });

        frequencs.iter().fold(vec![], |mut res, item| {
            for _ in 0..*item.1 {
                res.push(*item.0);
            }
            res
        })
    }
}

#[test]
fn test_frequency_sort() {
    assert_eq!(
        vec![3, 1, 1, 2, 2, 2],
        Solution::frequency_sort(vec![1, 1, 2, 2, 2, 3])
    );
    assert_eq!(
        vec![1, 3, 3, 2, 2],
        Solution::frequency_sort(vec![2, 3, 1, 3, 2])
    );
    assert_eq!(
        vec![5, -1, 4, 4, -6, -6, 1, 1, 1],
        Solution::frequency_sort(vec![-1, 1, -6, 4, 5, -6, 1, 4, 1])
    );
}
