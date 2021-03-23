struct Solution;

impl Solution {
    pub fn nearest_valid_point(x: i32, y: i32, points: Vec<Vec<i32>>) -> i32 {
        let mut distance = 0;
        let mut res = -1_i32;
        for (i, point) in points.iter().enumerate() {
            if x == point[0] || y == point[1] {
                let current_d = (point[0] - x).abs() + (point[1] - y).abs();
                if res == -1 || current_d < distance {
                    res = i as i32;
                    distance = current_d;
                }
            }
        }
        res
    }
}

#[test]
fn test_nearest_valid_point() {
    assert_eq!(
        2,
        Solution::nearest_valid_point(
            3,
            4,
            vec![vec![1, 2], vec![3, 1], vec![2, 4], vec![2, 3], vec![4, 4]]
        )
    );

    assert_eq!(0, Solution::nearest_valid_point(3, 4, vec![vec![3, 4]]));

    assert_eq!(-1, Solution::nearest_valid_point(3, 4, vec![vec![2, 3]]));
}
