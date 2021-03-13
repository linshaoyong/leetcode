struct Solution;

impl Solution {
    pub fn min_operations(logs: Vec<String>) -> i32 {
        let mut res = 0;
        for log in logs {
            match &log[..] {
                "../" => {
                    if res > 0 {
                        res -= 1;
                    }
                }
                "./" => {}
                _ => res += 1,
            }
        }
        res
    }
}

#[test]
fn test_min_operations() {
    assert_eq!(
        2,
        Solution::min_operations(vec![
            "d1/".to_string(),
            "d2/".to_string(),
            "../".to_string(),
            "d21/".to_string(),
            "./".to_string()
        ])
    );
    assert_eq!(
        3,
        Solution::min_operations(vec![
            "d1/".to_string(),
            "d2/".to_string(),
            "./".to_string(),
            "d3/".to_string(),
            "../".to_string(),
            "d31/".to_string()
        ])
    );
    assert_eq!(
        0,
        Solution::min_operations(vec![
            "d1/".to_string(),
            "../".to_string(),
            "../".to_string(),
            "../".to_string()
        ])
    );
}
