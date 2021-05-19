struct Solution;

impl Solution {
    pub fn min_eating_speed(piles: Vec<i32>, h: i32) -> i32 {
        let piles_cloned = &piles.clone();
        let mut left = 1;
        let mut right = *piles.iter().max().unwrap();
        while left < right {
            let mid = left + (right - left) / 2;
            if feasible(mid, h, piles_cloned) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        left
    }
}

fn feasible(speed: i32, h: i32, piles: &Vec<i32>) -> bool {
    let mut hours = 0;
    for pile in piles {
        hours += (pile - 1) / speed + 1;
        if hours > h {
            return false;
        }
    }
    true
}

#[test]
fn test_min_eating_speed() {
    assert_eq!(4, Solution::min_eating_speed(vec![3, 6, 7, 11], 8));
    assert_eq!(30, Solution::min_eating_speed(vec![30, 11, 23, 4, 20], 5));
    assert_eq!(23, Solution::min_eating_speed(vec![30, 11, 23, 4, 20], 6));
}
