use std::collections::HashSet;

struct Solution;

impl Solution {
    pub fn find_circle_num(is_connected: Vec<Vec<i32>>) -> i32 {
        let mut matrix = &is_connected.clone();
        let visited = &mut vec![0; matrix.len()];
        let mut count = 0;
        for i in 0..matrix.len() {
            if (visited[i] == 0) {
                Solution::dfs(matrix, visited, i);
                count += 1;
            }
        }
        count
    }

    fn dfs(matrix: &Vec<Vec<i32>>, visited: &mut Vec<usize>, i: usize) {
        for j in 0..matrix.len() {
            if (matrix[i][j] == 1 && visited[j] == 0) {
                visited[j] = 1;
                Solution::dfs(matrix, visited, j);
            }
        }
    }
}

#[test]
fn test_find_circle_num() {
    assert_eq!(
        2,
        Solution::find_circle_num(vec![vec![1, 1, 0], vec![1, 1, 0], vec![0, 0, 1]])
    );
    assert_eq!(
        3,
        Solution::find_circle_num(vec![vec![1, 0, 0], vec![0, 1, 0], vec![0, 0, 1]])
    );
    assert_eq!(
        1,
        Solution::find_circle_num(vec![
            vec![1, 0, 0, 1],
            vec![0, 1, 1, 0],
            vec![0, 1, 1, 1],
            vec![1, 0, 1, 1]
        ])
    );
}
