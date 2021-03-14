use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn sum_of_unique(nums: Vec<i32>) -> i32 {
        let mut map = HashMap::<i32, i32>::new();
        for num in nums {
            *map.entry(num).or_insert(0) += 1;
        }
        map.iter().fold(0, |mut acc, (k, v)| {
            if *v == 1 {
                acc += k;
            }
            acc
        })
    }
}

#[test]
fn test_sum_of_unique() {
    assert_eq!(4, Solution::sum_of_unique(vec![1, 2, 3, 2]));
    assert_eq!(0, Solution::sum_of_unique(vec![1, 1, 1, 1, 1]));
    assert_eq!(15, Solution::sum_of_unique(vec![1, 2, 3, 4, 5]));
}
