struct Solution;

impl Solution {
    pub fn square_is_white(coordinates: String) -> bool {
        let bs = coordinates.as_bytes();
        bs[0] % 2 != bs[1] % 2
    }
}

#[test]
fn test_square_is_white() {
    assert_eq!(false, Solution::square_is_white("a1".to_string()));
    assert_eq!(true, Solution::square_is_white("h3".to_string()));
    assert_eq!(false, Solution::square_is_white("c7".to_string()));
}
