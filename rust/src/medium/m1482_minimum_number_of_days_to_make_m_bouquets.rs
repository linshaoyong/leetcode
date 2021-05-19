struct Solution;

impl Solution {
    pub fn min_days(bloom_day: Vec<i32>, m: i32, k: i32) -> i32 {
        if m * k > bloom_day.len() as i32 {
            return -1;
        }
        let bloom_day_cloned = &bloom_day.clone();
        let mut left: i32 = 1;
        let mut right: i32 = *bloom_day.iter().max().unwrap();
        while left < right {
            let mid = left + (right - left) / 2;
            if feasible(mid, m, k, bloom_day_cloned) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        left
    }
}

fn feasible(days: i32, m: i32, k: i32, bloom_day: &Vec<i32>) -> bool {
    let mut bonquets = 0;
    let mut flowers = 0;
    for bloom in bloom_day {
        if bloom > &days {
            flowers = 0
        } else {
            bonquets += (flowers + 1) / k;
            flowers = (flowers + 1) % k;
        }
    }
    bonquets >= m
}

#[test]
fn test_min_days() {
    assert_eq!(3, Solution::min_days(vec![1, 10, 3, 10, 2], 3, 1));
    assert_eq!(-1, Solution::min_days(vec![1, 10, 3, 10, 2], 3, 2));
    assert_eq!(12, Solution::min_days(vec![7, 7, 7, 7, 12, 7, 7], 2, 3));
    assert_eq!(
        1000000000,
        Solution::min_days(vec![1000000000, 1000000000], 1, 1)
    );
    assert_eq!(
        9,
        Solution::min_days(vec![1, 10, 2, 9, 3, 8, 4, 7, 5, 6], 4, 2)
    );
}
