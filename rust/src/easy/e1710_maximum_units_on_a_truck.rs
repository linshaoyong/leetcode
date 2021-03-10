struct Solution;

impl Solution {
    pub fn maximum_units(box_types: Vec<Vec<i32>>, truck_size: i32) -> i32 {
        let mut res = 0;
        let mut tsize = truck_size;
        let mut cloned = box_types.clone();
        cloned.sort_by(|a, b| b[1].cmp(&a[1]));
        for box_type in cloned {
            if tsize <= 0 {
                break;
            }
            let n = if tsize > box_type[0] {
                box_type[0]
            } else {
                tsize
            };
            res += n * box_type[1];
            tsize -= box_type[0];
        }
        res
    }
}

#[test]
fn test_maximum_units() {
    assert_eq!(
        8,
        Solution::maximum_units(vec![vec![1, 3], vec![2, 2], vec![3, 1]], 4)
    );
    assert_eq!(
        91,
        Solution::maximum_units(vec![vec![5, 10], vec![2, 5], vec![4, 7], vec![3, 9]], 10)
    );
}
