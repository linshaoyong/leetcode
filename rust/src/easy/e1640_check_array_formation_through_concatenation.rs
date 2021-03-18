use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn can_form_array(arr: Vec<i32>, pieces: Vec<Vec<i32>>) -> bool {
        let mut res = true;
        let map: HashMap<&i32, usize> = arr.iter().enumerate().map(|(i, v)| (v, i)).collect();

        let arr_len = arr.len();
        let mut piece_len = 0;

        for piece in pieces {
            piece_len += piece.len();
            if !map.contains_key(&piece[0]) {
                return false;
            }
            let mut index = *map.get(&piece[0]).unwrap();
            for i in 1..piece.len() {
                if !map.contains_key(&piece[i]) {
                    return false;
                }
                let j = *map.get(&piece[i]).unwrap();
                if j != index + 1 {
                    return false;
                }
                index += 1;
            }
        }
        if arr_len != piece_len {
            return false;
        }
        true
    }
}

#[test]
fn test_can_form_array() {
    assert!(Solution::can_form_array(vec![85], vec![vec![85]]));
    assert!(Solution::can_form_array(
        vec![15, 88],
        vec![vec![88], vec![15]]
    ));
    assert!(Solution::can_form_array(vec![49, 18, 16], vec![vec![16, 18, 49]]) == false);
    assert!(Solution::can_form_array(
        vec![91, 4, 64, 78],
        vec![vec![78], vec![4, 64], vec![91]]
    ));
    assert!(Solution::can_form_array(vec![1, 3, 5, 7], vec![vec![2, 4, 6, 8]]) == false);
}
