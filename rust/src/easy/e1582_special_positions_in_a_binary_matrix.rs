struct Solution;

impl Solution {
    pub fn num_special(mat: Vec<Vec<i32>>) -> i32 {
        let mut res = 0;
        let mut row_sum = vec![0; mat.len()];
        let mut col_sum = vec![0; mat[0].len()];
        for i in 0..mat.len() {
            let row = &mat[i];
            for j in 0..row.len() {
                if row[j] == 1 {
                    row_sum[i] += 1;
                    col_sum[j] += 1;
                }
            }
        }
        for i in 0..mat.len() {
            let row = &mat[i];
            for j in 0..row.len() {
                if row[j] == 1 && row_sum[i] == 1 && col_sum[j] == 1 {
                    res += 1;
                }
            }
        }
        res
    }
}

#[test]
fn test_num_special() {
    assert_eq!(
        1,
        Solution::num_special(vec![vec![1, 0, 0], vec![0, 0, 1], vec![1, 0, 0]])
    );

    assert_eq!(
        3,
        Solution::num_special(vec![vec![1, 0, 0], vec![0, 1, 0], vec![0, 0, 1]])
    );

    assert_eq!(
        2,
        Solution::num_special(vec![
            vec![0, 0, 0, 1],
            vec![1, 0, 0, 0],
            vec![0, 1, 1, 0],
            vec![0, 0, 0, 0]
        ])
    );

    assert_eq!(
        3,
        Solution::num_special(vec![
            vec![0, 0, 0, 0, 0],
            vec![1, 0, 0, 0, 0],
            vec![0, 1, 0, 0, 0],
            vec![0, 0, 1, 0, 0],
            vec![0, 0, 0, 1, 1]
        ])
    );

    assert_eq!(
        1,
        Solution::num_special(vec![
            vec![0, 0, 0, 0, 0, 1, 0, 0],
            vec![0, 0, 0, 0, 1, 0, 0, 1],
            vec![0, 0, 0, 0, 1, 0, 0, 0],
            vec![1, 0, 0, 0, 1, 0, 0, 0],
            vec![0, 0, 1, 1, 0, 0, 0, 0]
        ])
    );
}
