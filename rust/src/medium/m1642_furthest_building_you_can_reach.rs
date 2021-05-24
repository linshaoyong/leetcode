struct Solution;

impl Solution {
    pub fn furthest_building(heights: Vec<i32>, bricks: i32, ladders: i32) -> i32 {
        let mut prev = heights[0];

        let mut distances = &mut vec![];
        for height in &heights {
            if height > &prev {
                distances.push(height - prev);
            } else {
                distances.push(0);
            }
            prev = *height;
        }

        let mut left = 0;
        let mut right = heights.len() as i32 - 1;
        while left < right {
            let mid = left + (right + 1 - left) / 2;
            if feasible(mid, distances, bricks, ladders) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        left
    }
}

fn feasible(m: i32, distances: &mut Vec<i32>, bricks: i32, ladders: i32) -> bool {
    let mut sd = &mut distances[..m as usize + 1];
    let mut mut_bricks = bricks.clone();
    let mut mut_ladders = ladders.clone();
    sd.sort();

    let mut indexes = -1 as i32;
    for distance in sd {
        if mut_bricks >= *distance {
            mut_bricks -= *distance;
            indexes += 1;
        } else {
            if mut_ladders > 0 {
                mut_ladders -= 1;
                indexes += 1;
            }
        }
        if indexes >= m {
            return true;
        }
    }
    false
}

#[test]
fn test_furthest_building() {
    assert_eq!(1, Solution::furthest_building(vec![7, 5, 13], 0, 0));
    assert_eq!(
        4,
        Solution::furthest_building(vec![4, 2, 7, 6, 9, 14, 12], 5, 1)
    );
    assert_eq!(
        7,
        Solution::furthest_building(vec![4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2)
    );
    assert_eq!(3, Solution::furthest_building(vec![14, 3, 19, 3], 17, 0));
}
