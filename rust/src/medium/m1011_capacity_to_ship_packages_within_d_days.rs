struct Solution;

impl Solution {
    pub fn ship_within_days(weights: Vec<i32>, days: i32) -> i32 {
        let mut low = weights.iter().max().unwrap().clone();
        let mut high: i32 = weights.iter().sum();

        while low < high {
            let mid = (low + high) / 2;
            let mut cap = 0;
            let mut need_days = 1;

            for weight in weights.iter() {
                if (cap + weight) > mid {
                    cap = 0;
                    need_days += 1;
                }
                cap += weight;
            }

            if need_days > days {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        low
    }
}

#[test]
fn test_ship_within_days() {
    assert_eq!(
        15,
        Solution::ship_within_days(vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
    );
    assert_eq!(6, Solution::ship_within_days(vec![3, 2, 2, 4, 1, 4], 3));
    assert_eq!(3, Solution::ship_within_days(vec![1, 2, 3, 1, 1], 4));
}
