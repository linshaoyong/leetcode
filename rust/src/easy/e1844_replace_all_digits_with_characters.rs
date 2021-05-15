struct Solution;

impl Solution {
    pub fn replace_digits(s: String) -> String {
        let mut res: Vec<char> = vec![];
        for c in s.chars() {
            if c.is_numeric() {
                let n = c.to_digit(10).unwrap() as u8;
                res.push((res[res.len() - 1] as u8 + n) as char);
            } else {
                res.push(c);
            }
        }
        res.iter().collect()
    }
}

#[test]
fn test_replace_digits() {
    assert_eq!("abcdef", Solution::replace_digits("a1c1e1".to_string()));
    assert_eq!(
        "abbdcfdhe",
        Solution::replace_digits("a1b2c3d4e".to_string())
    );
}
